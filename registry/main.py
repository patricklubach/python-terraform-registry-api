import uvicorn
from fastapi import FastAPI

from registry.api.routes.api import router
from registry.core.config import Config


def app():
    app = FastAPI(debug = True)
    app.include_router(router)
    return app


def main():
  uvicorn.run(
    "registry.main:app",
    host=Config.host,
    port=Config.port,
    factory=True,
    reload=Config.development
  )

if __name__ == "__main__":
    main()