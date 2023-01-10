import logging

import uvicorn.logging

from registry.core.config import Config

loglevel = {
  "INFO" : logging.INFO,
  "WARNING" : logging.WARNING,
  "ERROR" : logging.ERROR,
  "CRITICAL" : logging.CRITICAL,
  "DEBUG" : logging.DEBUG,
}

logger = logging.getLogger("uvicorn")
logger.setLevel(loglevel[Config.log_level])
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))
logger.addHandler(handler)

# Example:
# @router.get("/")
# async def hello():
#     logger.debug("This is a debug log message")
#     logger.info("This is an informational log message")
#     logger.warning("This is a warning log message")
#     logger.error("This is an error log message")
#     logger.critical("This is a critical log message")
#     return {"hello": "world"}