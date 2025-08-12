from fastapi import FastAPI
from app.api.routes import router as eda_vis_router

app = FastAPI(title="EDA & Visualisation API")
app.include_router(eda_vis_router)

@app.get("/health")
def health():
    return {"status": "ok"}