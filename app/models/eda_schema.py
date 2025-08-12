from pydantic import BaseModel
from typing import List, Dict, Any, Optional


# -------- EDA --------
class EDARequest(BaseModel):
    dataset_id: Optional[str] = None
    rows: Optional[List[Dict[str, Any]]] = None
    target_column: Optional[str] = None


class EDAResponse(BaseModel):
    summary: Dict[str, Any]
    correlations: Dict[str, float]