from __future__ import annotations

from collections.abc import Callable

from learnpy.lessons.advanced_python import context_manager_demo
from learnpy.lessons.async_demo import async_demo
from learnpy.lessons.basics import collections_demo, hello
from learnpy.lessons.logging_demo import logging_demo
from learnpy.lessons.oop import dataclasses_demo
from learnpy.lessons.variable_demo import variable_demo

LessonFn = Callable[[], None]


class LessonNotFoundError(RuntimeError):
    def __init__(self, lesson_id: str):
        super().__init__(f"Unknown lesson id: {lesson_id!r}. Run `learnpy list` to see options.")


_LESSONS: dict[str, LessonFn] = {
    "basics.hello": hello,
    "basics.collections": collections_demo,
    "basics.variables": variable_demo,
    "oop.dataclasses": dataclasses_demo,
    "logging.demo": logging_demo,
    "advanced.context_manager": context_manager_demo,
    "async.demo": async_demo,
}


def list_lessons() -> list[str]:
    return sorted(_LESSONS.keys())


def run_lesson(lesson_id: str) -> None:
    fn = _LESSONS.get(lesson_id)
    if fn is None:
        raise LessonNotFoundError(lesson_id)
    fn()
