from __future__ import annotations

import logging


def logging_demo() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(name)s: %(message)s",
    )
    log = logging.getLogger("learnpy")

    log.info("Logging is better than print for non-trivial apps.")
    log.warning("This is a warning example.")
