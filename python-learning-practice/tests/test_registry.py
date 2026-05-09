from __future__ import annotations

import learnpy.registry as reg


def test_list_lessons_sorted_and_nonempty() -> None:
    lessons = reg.list_lessons()
    assert lessons, "expected at least one lesson to exist"
    assert lessons == sorted(lessons)


def test_run_unknown_lesson_raises() -> None:
    try:
        reg.run_lesson("does.not.exist")
    except reg.LessonNotFoundError as e:
        assert "Unknown lesson id" in str(e)
    else:
        raise AssertionError("expected LessonNotFoundError")
