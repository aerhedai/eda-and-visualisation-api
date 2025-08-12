from fastapi import APIRouter, HTTPException
from app.models.eda_schema import EDARequest, EDAResponse
from app.services.eda_vis_service import compute_eda
from app.models.vis_schema import VisualisationRequest, VisualisationResponse
from app.services.eda_vis_service import create_plot
import pandas as pd
import os
from app.core.config import settings

router = APIRouter()

@router.post("/eda-insights", response_model=EDAResponse)
def eda_insights(req: EDARequest):
    rows = req.rows
    # If dataset_id provided, load from file
    if req.dataset_id:
        path = os.path.join(settings.DATA_DIR, f"{req.dataset_id}.csv")
        if not os.path.exists(path):
            raise HTTPException(status_code=404, detail="Dataset file not found")
        df = pd.read_csv(path)
        rows = df.to_dict(orient="records")
    
    if not rows:
        raise HTTPException(status_code=400, detail="No data provided for EDA")

    output = compute_eda(rows)
    return EDAResponse(summary=output["summary"], correlations=output["correlations"])


@router.post("/visualise", response_model=VisualisationResponse)
def visualise(req: VisualisationRequest):
    rows = req.rows
    if req.dataset_id:
        path = os.path.join(settings.DATA_DIR, f"{req.dataset_id}.csv")
        if not os.path.exists(path):
            raise HTTPException(status_code=404, detail="Dataset file not found")
        df = pd.read_csv(path)
        rows = df.to_dict(orient="records")

    if not rows:
        raise HTTPException(status_code=400, detail="No data provided for visualisation")

    img = create_plot(rows, req.chart_type, req.x, req.y)
    return VisualisationResponse(image_base64=img)
