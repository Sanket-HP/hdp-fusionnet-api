from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse
from src.model.hdpfusion import HDPFusionNet

app = FastAPI()
model = HDPFusionNet()

API_KEYS = ["HDP-KEY-12345", "HDP-KEY-67890"]

@app.post("/api/predict")
async def predict(text: str, authorization: str = Header(None)):
    if authorization not in API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    result = model.process(text)
    return JSONResponse({"prediction": result})

@app.get("/api/predict")
async def get_status():
    return {"status": "API is working!"}
