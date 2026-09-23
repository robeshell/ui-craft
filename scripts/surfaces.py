#!/usr/bin/env python3
"""Generate brand-tinted neutral surfaces and text colors, light and dark.

Takes one brand color, keeps its hue, and produces a low-chroma neutral
ladder in OKLCH: page background, content surface, raised layer, overlay,
plus primary / secondary / tertiary text. Text colors are pushed darker
(light mode) or lighter (dark mode) until they reach 4.5:1 on the least
favourable surface they may sit on. Values are provisional baselines to be
replaced by project tokens; standard library only.
"""
import argparse
import json
import re
import sys

# ---------- sRGB <-> OKLab ----------

def hex_to_rgb(value):
    value = value.strip()
    m = re.fullmatch(r"#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", value)
    if not m:
        raise argparse.ArgumentTypeError("Use #RGB or #RRGGBB: %s" % value)
    digits = m.group(1)
    if len(digits) == 3:
        digits = "".join(ch * 2 for ch in digits)
    return tuple(int(digits[i:i + 2], 16) / 255 for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#%02X%02X%02X" % tuple(round(max(0.0, min(1.0, c)) * 255) for c in rgb)


def to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def to_gamma(c):
    c = max(0.0, min(1.0, c))
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def rgb_to_oklab(rgb):
    r, g, b = (to_linear(c) for c in rgb)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = (x ** (1 / 3) if x >= 0 else -((-x) ** (1 / 3)) for x in (l, m, s))
    return (0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
            1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
            0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s)


def oklab_to_rgb(lab):
    L, a, b = lab
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    r = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bb = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return tuple(to_gamma(c) for c in (r, g, bb))


def oklch_to_rgb(L, C, h_deg):
    import math
    h = math.radians(h_deg)
    return oklab_to_rgb((L, C * math.cos(h), C * math.sin(h)))


def hue_of(rgb):
    import math
    _, a, b = rgb_to_oklab(rgb)
    return math.degrees(math.atan2(b, a)) % 360


# ---------- WCAG contrast ----------

def luminance(rgb):
    r, g, b = (to_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)))
    return (lb + 0.05) / (la + 0.05)


# ---------- ladder ----------

LIGHT = {
    "surfaces": [("page", 0.965), ("surface", 1.0), ("raised", 1.0), ("overlay", 1.0)],
    "text": [("text_primary", 0.25), ("text_secondary", 0.47), ("text_tertiary", 0.56)],
    "surface_chroma": 0.004,
    "text_chroma": 0.008,
    "text_step": -0.005,   # darken until it passes
    "worst_surface": "page",
}
DARK = {
    "surfaces": [("page", 0.20), ("surface", 0.24), ("raised", 0.28), ("overlay", 0.32)],
    "text": [("text_primary", 0.96), ("text_secondary", 0.80), ("text_tertiary", 0.66)],
    "surface_chroma": 0.006,
    "text_chroma": 0.006,
    "text_step": 0.005,    # lighten until it passes
    "worst_surface": "overlay",
}


def build(mode, hue, target):
    surfaces = {name: oklch_to_rgb(L, mode["surface_chroma"], hue) for name, L in mode["surfaces"]}
    worst = surfaces[mode["worst_surface"]]
    text = {}
    for name, L in mode["text"]:
        rgb = oklch_to_rgb(L, mode["text_chroma"], hue)
        guard = 0
        while contrast(rgb, worst) < target and guard < 200:
            L += mode["text_step"]
            rgb = oklch_to_rgb(L, mode["text_chroma"], hue)
            guard += 1
        text[name] = rgb
    out = {"surfaces": {k: rgb_to_hex(v) for k, v in surfaces.items()},
           "text": {k: rgb_to_hex(v) for k, v in text.items()},
           "contrast": {}}
    for tname, trgb in text.items():
        out["contrast"][tname] = {sname: round(contrast(trgb, srgb), 2) for sname, srgb in surfaces.items()}
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("brand", type=hex_to_rgb, help="brand color, #RRGGBB")
    parser.add_argument("--target", type=float, default=4.5,
                        help="minimum contrast for text on the least favourable surface (default 4.5)")
    parser.add_argument("--json", action="store_true", help="print JSON only")
    args = parser.parse_args()

    hue = hue_of(args.brand)
    result = {
        "brand": rgb_to_hex(args.brand),
        "hue_deg": round(hue, 1),
        "note": "Provisional baselines. Contrast is WCAG 2.x at full precision; text colors were adjusted to reach the target on the least favourable surface.",
        "light": build(LIGHT, hue, args.target),
        "dark": build(DARK, hue, args.target),
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print("brand %s  hue %.1f°" % (result["brand"], hue))
    for mode in ("light", "dark"):
        block = result[mode]
        print("\n[%s]" % mode)
        for name, value in block["surfaces"].items():
            print("  %-15s %s" % (name, value))
        for name, value in block["text"].items():
            ratios = "  ".join("%s %.2f" % (s, r) for s, r in block["contrast"][name].items())
            print("  %-15s %s   %s" % (name, value, ratios))
    return 0


if __name__ == "__main__":
    sys.exit(main())
