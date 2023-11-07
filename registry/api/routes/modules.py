import copy
import datetime
import os
import re
import uuid
from typing import List

from fastapi import APIRouter, Response, UploadFile

from registry.models.module import Module
from registry.models.modules import Meta, ModuleResponse

router = APIRouter()

module_db: List[Module] = []


def _filter_by_namespace(modules: List[Module], namespace: str) -> List[Module]:
    for module in modules:
        if module.namespace != namespace:
            modules.remove(module)
    return modules


def _filter_by_provider(modules: List[Module], provider: str) -> List[Module]:
    for module in modules:
        if module.provider != provider:
            modules.remove(module)
    return modules


def _filter_by_verified(modules: List[Module]) -> List[Module]:
    for module in modules:
        if not module.verified:
            modules.remove(module)
    return modules


@router.get("/")
async def list_modules(offset: int = 0, provider: str = "", verified: bool = False):
    modules = copy.deepcopy(module_db)

    if provider:
        modules = _filter_by_provider(modules, provider)

    if verified:
        modules = _filter_by_verified(modules, verified)

    return ModuleResponse(
        meta=Meta(
            limit=offset,
            current_offset=0,
            next_offset=offset,
            next_url=f"/v1/modules?limit={offset}&offset={offset}&verified={str(verified).lower()}",
        ),
        modules=modules,
    )


@router.get("/{namespace}")
async def list_modules_by_namespace(
    namespace, offset: int = 0, provider: str = "", verified: bool = False
):
    modules: List[Module] = []

    for module in module_db:
        if module.namespace == namespace:
            modules.append(module)

    if provider:
        modules = _filter_by_provider(modules, provider)

    if verified:
        modules = _filter_by_verified(modules, verified)

    return ModuleResponse(
        meta=Meta(
            limit=offset,
            current_offset=0,
            next_offset=offset,
            next_url=f"/v1/modules?limit={offset}&offset={offset}&verified={str(verified)}",
        ),
        modules=modules,
    )


@router.get("/search")
async def search_modules(
    q: str,
    offset: int = 0,
    provider: str = "",
    namespace: str = "",
    verified: bool = False,
):
    modules: List[Module] = []

    for module in module_db:
        if re.search(q, module.name):
            modules.append(module)

    if namespace:
        modules = _filter_by_namespace(modules, namespace)

    if provider:
        modules = _filter_by_provider(modules, provider)

    if verified:
        modules = _filter_by_verified(modules, verified)

    return ModuleResponse(
        meta=Meta(
            limit=offset,
            current_offset=0,
            next_offset=offset,
            next_url=f"/v1/modules?limit={offset}&offset={offset}&verified={str(verified)}",
        ),
        modules=modules,
    )


@router.get("/{namespace}/{name}/{provider}/versions")
async def list_module_versions(namespace: str, name: str, provider: str):
    modules = [
        module
        for module in module_db
        if module.namespace == namespace
        and module.name == name
        and module.provider == provider
    ]
    return {"modules": modules}


@router.get("/{namespace}/{name}")
async def list_latest_module_version_foreach_provider(namespace: str, name: str, offset: int = 0):
    modules = [
        module
        for module in module_db
        if module.namespace == namespace and module.name == name
    ]

    return ModuleResponse(Meta(limit=0, current_offset=0), modules)


@router.get("/{namespace}/{name}/{provider}/{version}/download")
async def download_specific_module_version(
    namespace: str, name: str, provider: str, version: str
):
    for module in module_db:
        if (
            module.namespace == namespace
            and module.name == name
            and module.provider == provider
            and module.version == version
        ):
            url = module.url
            break

    return Response(status_code=204, headers={"X-Terraform-Get": url})


@router.get("/{namespace}/{name}/{provider}/download")
async def download_latest_module_version(namespace: str, name: str, provider: str):
    for module in module_db:
        if (
            module.namespace == namespace
            and module.name == name
            and module.provider == provider
            and module.latest
        ):
            url = module.url
            break

    return Response(status_code=204, headers={"X-Terraform-Get": url})


@router.get("/{namespace}/{name}/{provider}")
async def get_latest_module_version_by_provider(
    namespace: str, name: str, provider: str
):
    for module in module_db:
        if (
            module.namespace == namespace
            and module.name == name
            and module.provider == provider
            and module.latest
        ):
            return module
    return {}


@router.get("/{namespace}/{name}/{provider}/{version}")
async def get_module(namespace: str, name: str, provider: str, version: str):
    for module in module_db:
        if (
            module.namespace == namespace
            and module.name == name
            and module.provider == provider
            and module.version == version
        ):
            return module
    return {}


@router.post("/{namespace}/{name}/{provider}/vcs")
def create_module_vcs(namespace: str, name: str, provider: str):
    return {}


@router.put("/{namespace}/{name}/{provider}/novcs")
def create_module_latest_no_vcs(namespace: str, name: str, provider: str, file: UploadFile):
    try:
        path = f"data/{namespace}/{name}/{provider}/latest/"
        os.makedirs(path, exist_ok=True)

        filepath = f"{path}/archive.tar.gz"
        with open(filepath, "wb") as f:
            f.write(file.file.read())

    except Exception as err:
        return {"error": err}

    return {"filename": file.filename}


@router.put("/{namespace}/{name}/{provider}/{version}/novcs")
def create_module_version_no_vcs(namespace: str, name: str, provider: str, version: str, file: UploadFile):
    try:
        # module = Module(
        #     id=uuid.uuid4(),
        #     owner="",
        #     namespace=namespace,
        #     name=name,
        #     provider=provider,
        #     version=version,
        #     is_latest=False,
        #     description="",
        #     source="upload",
        #     created_at=datetime.fromtimestamp(datetime.timestamp(datetime.now()), tz=datetime.tzinfo).strftime("%Y-%m-%dT%H:%M:%S.%fZ%z"),
        #     download_url=f"http://127.0.0.1:8000/v1/modules/{namespace}/{name}/{provider}/{version}/download")

        path = f"data/{namespace}/{name}/{provider}/{version}"
        os.makedirs(path, exist_ok=True)

        filepath = f"{path}/archive.tar.gz"
        with open(filepath, "wb") as f:
            f.write(file.file.read())

    except Exception as err:
        return {"error": err}

    return {"filename": file.filename}
