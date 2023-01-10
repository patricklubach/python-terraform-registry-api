# from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Module(BaseModel):
    id: str
    owner: str
    namespace: str
    name: str
    provider: str
    version: str
    is_latest: bool
    description: str
    source: str
    created_at: str
    updated_at: Optional[str]
    downloads: Optional[int]
    download_url: str
