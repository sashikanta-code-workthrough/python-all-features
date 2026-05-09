from __future__ import annotations

import asyncio


async def _worker(name: str, delay_s: float) -> str:
    await asyncio.sleep(delay_s)
    return f"{name} done after {delay_s:.1f}s"


def async_demo() -> None:
    async def _main() -> None:
        results = await asyncio.gather(
            _worker("task-1", 0.2),
            _worker("task-2", 0.1),
        )
        for r in results:
            print(r)

    asyncio.run(_main())
