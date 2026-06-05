import sys
import argparse

from .ufo import animate_ufo


def main():
    parser = argparse.ArgumentParser(
        description="ufosay - a flying saucer terminal animation tool",
    )
    parser.add_argument(
        "message", nargs="?", default=None,
        help="message to display in the speech bubble",
    )
    parser.add_argument(
        "--msg", default=None,
        help="alternative way to provide the message",
    )
    args = parser.parse_args()

    msg = args.msg or args.message

    if msg is None and not sys.stdin.isatty():
        msg = sys.stdin.read().strip()

    animate_ufo(msg)
