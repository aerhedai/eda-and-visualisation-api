from pydantic import BaseModel
from typing import List, Dict, Any

class EDARequest(BaseModel):
    rows: List[Dict[str, Any]]

class EDAResponse(BaseModel):
    summary: Dict[str, Any]
    correlations: Dict[str, float]
