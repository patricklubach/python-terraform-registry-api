from fastapi import APIRouter

router = APIRouter()


@router.get("/{namespace}/{name}")
async def provider():
    address = os.environ.get("TFR_ADDRESS", default="0.0.0.0")
    port = os.environ.get("TFR_PORT", default=8080)

    return {"provider": "Hello World"}
