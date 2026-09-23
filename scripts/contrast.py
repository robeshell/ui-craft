#!/usr/bin/env python3
"""WCAG 2.x contrast ratio of two sRGB colors.

Accepts #RGB, #RRGGBB, #RRGGBBAA, rgb(r,g,b) and rgba(r,g,b,a).
Translucent colors are composited onto the page color given with --over
(background first, then foreground on top of the resulting background).
The result describes one color pair only; it makes no whole-product claim.
"""
import argparse
import json
import re
import sys

HEX = re.compile(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
RGB = re.compile(
    r"rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*(?:,\s*([01]?(?:\.\d+)?|\d{1,3}%)\s*)?\)$",
    re.IGNORECASE,
)


def parse(value):
    """Return (r, g, b, a) with channels in 0..255 and alpha in 0..1."""
    value = value.strip()
    m = HEX.match(value)
    if m:
        digits = m.group(1)
        if len(digits) == 3:
            digits = "".join(ch * 2 for ch in digits)
        r, g, b = (int(digits[i:i + 2], 16) for i in (0, 2, 4))
        a = int(digits[6:8], 16) / 255 if len(digits) == 8 else 1.0
        return r, g, b, a
    m = RGB.match(value)
    if m:
        r, g, b = (int(m.group(i)) for i in (1, 2, 3))
        if max(r, g, b) > 255:
            raise argparse.ArgumentTypeError("rgb channels must be 0..255: %s" % value)
        alpha = m.group(4)
        if alpha is None:
            a = 1.0
        elif alpha.endswith("%"):
            a = int(alpha[:-1]) / 100
        else:
            a = float(alpha)
        if not 0 <= a <= 1:
            raise argparse.ArgumentTypeError("alpha must be 0..1: %s" % value)
        return r, g, b, a
    raise argparse.ArgumentTypeError(
        "Use #RGB, #RRGGBB, #RRGGBBAA, rgb(r,g,b) or rgba(r,g,b,a): %s" % value
    )


def composite(top, bottom):
    """Source-over: top (with alpha) on an opaque bottom."""
    a = top[3]
    return tuple(round(top[i] * a + bottom[i] * (1 - a)) for i in range(3)) + (1.0,)


def to_hex(color):
    return "#%02X%02X%02X" % color[:3]


def luminance(color):
    channels = [c / 255 for c in color[:3]]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
              for c in channels]
    return sum(c * w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(first, second):
    low, high = sorted((luminance(first), luminance(second)))
    return (high + 0.05) / (low + 0.05)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("foreground", type=parse, help="text or icon color")
    parser.add_argument("background", type=parse, help="the surface directly behind it")
    parser.add_argument("--over", type=parse, default=None,
                        help="opaque page color under a translucent background")
    args = parser.parse_args()

    fg, bg, page = args.foreground, args.background, args.over
    if page is not None and page[3] < 1:
        parser.error("--over must be opaque")
    if bg[3] < 1:
        if page is None:
            parser.error("background is translucent; pass the page color with --over")
        bg = composite(bg, page)
    if fg[3] < 1:
        fg = composite(fg, bg)

    ratio = contrast(fg, bg)
    print(json.dumps({
        "foreground": to_hex(fg),
        "background": to_hex(bg),
        "ratio": ratio,
        "ratio_display": "%.2f:1" % ratio,
        "meets_4_5_normal_text": ratio >= 4.5,
        "meets_3_large_text_or_ui": ratio >= 3,
        "scope": "One opaque pair after compositing. Pick the applicable threshold yourself."
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
