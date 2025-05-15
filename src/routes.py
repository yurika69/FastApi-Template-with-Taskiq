import logging
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.DEBUG
)
logger = logging.getLogger(__name__)
load_dotenv()
router = APIRouter()

API_KEY = os.getenv("API_KEY")

api_key_header = APIKeyHeader(name="X-API-Key")
def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )
    return api_key

@router.post("/test")
async def test(api_key: str = Depends(get_api_key)):
    try:
        return JSONResponse(
            status_code=status.HTTP_202_ACCEPTED,
            content={"status": "ok", "message": f"hello"},
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"status": "error", "message": f"error, {e}"},
        )
    
