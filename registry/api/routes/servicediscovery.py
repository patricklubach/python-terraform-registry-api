import json
import os

from fastapi import APIRouter, HTTPException

from registry.core.log import logger

router = APIRouter()


@router.get("/.well-known/terraform.json")
def service_discovery():
    discovery_file = (
        f"{os.path.dirname(os.path.realpath(__file__))}/../../terraform.json"
    )
    try:
        with open(discovery_file, "r", encoding="utf-8") as discovery_file:
            return json.load(discovery_file)
    except FileNotFoundError as err:
        logger.error(err)
        raise HTTPException(
            status_code=500,
            detail="Internal server error. Please contact the administrator of this Registry.",
        ) from err
