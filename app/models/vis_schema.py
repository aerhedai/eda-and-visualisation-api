from pydantic import BaseModel
from typing import List, Dict, Any

class VisualisationRequest(BaseModel):
    rows: List[Dict[str, Any]]
    chart_type: str  # e.g., "histogram", "scatter"
    x: str
    y: str = None

class VisualisationResponse(BaseModel):
    image_base64: str  # encoded plot image
