# learnpy — Python Learning & Practice (Best Standards)

This repository is a **learning-first** Python project that also follows **real-world standards**: `src/` layout, type-checking, lint/format, tests, and CI-ready workflows.

It’s designed so you can:
- Learn Python from **basics → advanced**
- Practice by editing small modules under `src/learnpy/lessons/`
- Run examples and mini-exercises through a simple CLI: `learnpy`

---

## Quick start (beginner-friendly)

### Prerequisites
- Python **3.11+** (recommended: 3.12+)

### Create a virtual environment

```bash
cd python-learning-practice
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

### Install the project (editable) + dev tools

```bash
pip install -e ".[dev]"
```

### Run the CLI

```bash
learnpy --help
learnpy list
learnpy run basics.hello
```

---

## Project structure (recommended “src layout”)

```
python-learning-practice/
  src/
    learnpy/                 # installable package
      lessons/               # learning modules (your practice area)
  tests/                     # automated tests (pytest)
  docs/                      # optional notes (keep README as primary guide)
  scripts/                   # helper scripts (optional)
  pyproject.toml             # single source of truth for tooling + metadata
```

Why `src/` layout?
- It prevents accidentally importing your package from the working directory in a way that hides packaging mistakes.
- It matches how real packages are built and distributed.

---

## How to use this repo (learning path)

### 1) Basics (core language)
Start with:
- Variables, types, and operators
- Control flow: `if/elif/else`, `for`, `while`, `match`
- Functions: parameters, return values, scope
- Collections: `list`, `tuple`, `dict`, `set`

Try:
- `learnpy run basics.hello`
- `learnpy run basics.collections`

Where to practice:
- `src/learnpy/lessons/basics.py`

### 2) Data model and “Pythonic” patterns
Learn:
- Iteration protocol (`__iter__`, `__next__`)
- Context managers (`with`, `__enter__`, `__exit__`)
- Errors/exceptions: `try/except/else/finally`, custom exceptions

Practice:
- Add a small iterator in `src/learnpy/lessons/advanced_python.py`
- Add a custom exception class in `src/learnpy/lessons/errors.py`

### 3) OOP (when it helps)
Focus on:
- Classes, instances, and methods
- `@dataclass`
- Composition over inheritance
- ABCs / Protocols (interfaces)

Practice:
- `learnpy run oop.dataclasses`
- Extend `src/learnpy/lessons/oop.py`

### 4) Type hints (professional Python)
You’ll use:
- Built-in generics: `list[int]`, `dict[str, int]`
- `typing` tools: `Optional`, `Callable`, `Iterable`, `Protocol`
- Narrowing and `TypeGuard` (advanced)

Run type-checking:

```bash
mypy src
```

### 5) Testing (confidence + speed)
Learn:
- Unit tests with `pytest`
- Arrange/Act/Assert pattern
- Parametrization

Run tests:

```bash
pytest
```

Add your own tests in `tests/`.

### 6) Logging (debugging like a pro)
Use `logging` instead of print for non-trivial programs.

Practice:
- `learnpy run logging.demo`
- Edit `src/learnpy/lessons/logging_demo.py`

### 7) Async & concurrency (advanced)
Learn:
- `async` / `await`
- `asyncio` tasks
- When NOT to use async (CPU-bound workloads)

Practice:
- `learnpy run async.demo`
- Edit `src/learnpy/lessons/async_demo.py`

---

## Developer workflow (best standards)

### Formatting + linting (Ruff)

```bash
ruff format .
ruff check .
```

### Type-checking (mypy)

```bash
mypy src
```

### Run everything (recommended before commits)

```bash
ruff format .
ruff check .
mypy src
pytest
```

---

## CLI commands

### List available lessons

```bash
learnpy list
```

### Run a lesson by id

```bash
learnpy run basics.hello
learnpy run oop.dataclasses
```

### Add your own lesson

1. Create a new module in `src/learnpy/lessons/` (or edit an existing one).
2. Register a callable in `src/learnpy/registry.py`.
3. Run it:

```bash
learnpy run your_topic.your_lesson
```

---

## Common Python topics to practice next (ideas)

- **File I/O**: CSV/JSON, pathlib, streaming reads
- **HTTP**: `urllib` basics, then `httpx` (optional)
- **Packaging**: versioning, optional deps, publishing (later)
- **Performance**: profiling, big-O thinking, avoiding needless work
- **Security**: secrets management, avoiding `eval`, safe subprocess usage

---

## Troubleshooting

- **`learnpy: command not found`**: make sure your venv is activated and you ran `pip install -e ".[dev]"`.
- **Import errors**: run from the repo root and ensure you installed editable mode.
- **mypy is strict**: that’s intentional for learning. You can relax rules in `pyproject.toml` later.

---

## License

MIT — see `pyproject.toml`.

