#!/usr/bin/env python3
"""Print a chosen emoji and optional message from the command line"""

import argparse
from emoji import emojize
from rich import print

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="emoji function") # TODO: replace None with a helpful description of the f(x)
    parser.add_argument("--name", default=":rocket:", help="Emoji name (e.g., ':rocket:')") # TODO: default like ":rocket:" and a clear help string
    parser.add_argument("--msg", default="", help="Optional message to display with emoji") # TODO: default empty string and clear help
    return parser

def render_emoji(name: str, msg: str) -> str:
    """Return the combined emoji + message string."""
    symbol = emojize(name, language="alias") # DO NOT Change this line the first None is needed
    output = f"{symbol} {msg}".rstrip() # TODO: build f-string combining symbol + msg (strip trailing spaces)
    return output

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    
    # TODO: ensure args.name and args.msg become strings
    name = str(args.name)
    msg = str(args.msg)
    result = render_emoji(name, msg)
    print(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())