#!/usr/bin/env python3
"""Contrast of two opaque sRGB colors; no whole-product compliance claims."""
import argparse
import json
import re


def color(value):
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        raise argparse.ArgumentTypeError("Use opaque #RRGGBB; composite alpha colors first.")
    return value.upper()


def luminance(value):
    channels = [int(value[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
              for c in channels]
    return sum(c * weight for c, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(first, second):
    low, high = sorted((luminance(first), luminance(second)))
    return (high + 0.05) / (low + 0.05)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("foreground", type=color)
    parser.add_argument("background", type=color)
    args = parser.parse_args()
    ratio = contrast(args.foreground, args.background)
    print(json.dumps({
        "foreground": args.foreground,
        "background": args.background,
        "ratio": ratio,
        "meets_4_5": ratio >= 4.5,
        "meets_3": ratio >= 3,
        "scope": "Opaque color pair only. Select the applicable threshold separately."
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
