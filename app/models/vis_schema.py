from pydantic import BaseModel
from typing import List, Dict, Any, Optional

# -------- Visualisation --------
class VisualisationRequest(BaseModel):
    dataset_id: Optional[str] = None
    rows: Optional[List[Dict[str, Any]]] = None
    chart_type: str  # e.g., "histogram", "scatter"
    x: str
    y: Optional[str] = None


class VisualisationResponse(BaseModel):
    image_base64: str  # encoded plot image