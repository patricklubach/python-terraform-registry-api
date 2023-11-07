import uvicorn
from fastapi import FastAPI
from uvicorn import Config, Server

from registry.api.routes.api import router
from registry.core.config import Config as RegistryConfig


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(debug=True)
    app.include_router(router)
    return app


def main() -> None:
    server_config: Config = uvicorn.Config(
        "registry.main:create_app",
        host=RegistryConfig.host,
        port=RegistryConfig.port,
        reload=RegistryConfig.development,
        log_level=RegistryConfig.log_level,
        access_log=True,
        factory=True,
        use_colors=False,
    )
    server: Server = uvicorn.Server(config=server_config)
    server.run()


if __name__ == "__main__":
    main()
