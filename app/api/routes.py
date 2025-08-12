from fastapi import APIRouter
from app.models.eda_schema import EDARequest, EDAResponse
from app.models.vis_schema import VisualisationRequest, VisualisationResponse
from app.services.eda_vis_service import compute_eda, create_plot

router = APIRouter()

@router.post("/eda-insights", response_model=EDAResponse)
def eda_insights(req: EDARequest):
    output = compute_eda(req.rows)
    return EDAResponse(summary=output["summary"], correlations=output["correlations"])

@router.post("/visualise", response_model=VisualisationResponse)
def visualise(req: VisualisationRequest):
    img = create_plot(req.rows, req.chart_type, req.x, req.y)
    return VisualisationResponse(image_base64=img)
