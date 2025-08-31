import logging
from typing import Dict

from fastapi import APIRouter, Request

from app.core.third_party_integrations.crime_data.client import CrimeDataClient

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/crime-data", tags=["crime_data-proxy"])


# Utility

def proxy_get(path: str, params: Dict) -> Dict:
    client = CrimeDataClient()
    return client.get(path, params=params)


# Routes
@router.get("/health")
async def health() -> Dict:
    client = CrimeDataClient()
    return {
        "healthy": client.health(),
        "base_url": client.base_url,
        "has_api_key": bool(client.api_key),
    }

@router.get("/{path:path}")
async def crime_data_get(path: str, request: Request) -> Dict:
    return proxy_get(path, dict(request.query_params))
