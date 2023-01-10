import json
import os

from fastapi import APIRouter

router = APIRouter()

@router.get("/.well-known/terraform.json")
def service_discovery():
    discovery_file = f"{os.path.dirname(os.path.realpath(__file__))}/../terraform.json"
    print("HELLO")
    with open(discovery_file, "r") as discovery_file:
        return json.load(discovery_file)