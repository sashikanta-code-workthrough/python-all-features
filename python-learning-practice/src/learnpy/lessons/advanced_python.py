from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def chdir(path: Path) -> Iterator[None]:
    import os

    old = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)


def context_manager_demo() -> None:
    here = Path.cwd()
    tmp = here
    print("cwd before:", Path.cwd())
    with chdir(tmp):
        print("cwd inside:", Path.cwd())
    print("cwd after:", Path.cwd())
