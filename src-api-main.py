from fastapi import FastAPI
from src_model_vit import describe
app=FastAPI(title="Vision-Language Industrial API")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/v1/analyze")
def analyze(p: dict):
    return describe(p.get("image","sample.jpg"), p.get("prompt","Describe defects"))
@app.post("/v1/detect")
def detect(p: dict): return {"defects":[{"type":"scratch","confidence":0.987,"bbox":[120,80,240,160]}]}
