from __future__ import annotations

import argparse
import sys

from learnpy.registry import LessonNotFoundError, list_lessons, run_lesson


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="learnpy",
        description="Learning & practice CLI for the learnpy project.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="List available lessons.")
    p_list.set_defaults(_handler=_cmd_list)

    p_run = sub.add_parser("run", help="Run a lesson by id (example: basics.hello).")
    p_run.add_argument("lesson_id", help="Lesson identifier, e.g. basics.hello")
    p_run.set_defaults(_handler=_cmd_run)

    return parser


def _cmd_list(_: argparse.Namespace) -> int:
    for lesson_id in list_lessons():
        print(lesson_id)
    return 0


def _cmd_run(args: argparse.Namespace) -> int:
    try:
        run_lesson(args.lesson_id)
    except LessonNotFoundError as e:
        print(str(e), file=sys.stderr)
        return 2
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    return int(args._handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
