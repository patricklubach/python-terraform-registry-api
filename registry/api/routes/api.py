from fastapi import APIRouter

from registry.api.routes import modules, providers, servicediscovery

router = APIRouter()

router.include_router(servicediscovery.router)
router.include_router(modules.router, prefix="/v1/modules")
router.include_router(providers.router, prefix="/v1/provider")