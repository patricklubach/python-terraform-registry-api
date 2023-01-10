from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel

from registry.models.module import Module


class Provider(BaseModel):
    name: str
    version: str


class Submodule(BaseModel):
    path: str
    providers: List[Provider]
    dependencies: Optional[List[Any]]


class Version(BaseModel):
    version: str
    submodules: Optional[List[Submodule]]


# class Module(BaseModel):
#     id: str
#     owner: str
#     namespace: str
#     name: str
#     version: str
#     provider: str
#     provider_logo_url: str
#     description: str
#     source: str
#     tag: str
#     published_at: str
#     downloads: int
#     verified: bool
#     url: str
#     latest: bool


class ModuleVersions(BaseModel):
    source: str
    versions: List[Version]


class Meta(BaseModel):
    limit: int
    current_offset: int
    next_offset: Optional[int]
    next_url: Optional[str]
    prev_offset: Optional[int]


class ModuleResponse(BaseModel):
    meta: Dict[str, Union[int, str]]
    modules: Union[List[Module], ModuleVersions]


class ModuleCreationAttributes(BaseModel):
    name: str
    provider: str
    namespace: str
    registry_name: str
    no_code: bool


class ModuleCreationNoVCSRequest(BaseModel):
    namespace: str
    name: str
    provider: str
    type: str
    attributes: ModuleCreationAttributes


class ModuleCreationNoVCSResponseAttributes(BaseModel):
    name: str
    namespace: str
    registry_name: str
    provider: str
    status: str
    version_statuses: List[str]
    created_at: str
    updated_at: str
    permissions: Dict[str, bool]


class ModuleCreationNoVCSResponseData(BaseModel):
    id: str
    type : str
    attributes: ModuleCreationNoVCSResponseAttributes


class ModuleCreationNoVCSResponse(BaseModel):
    data : ModuleCreationNoVCSResponseData
