from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from starlette.responses import Response
import psutil

app = FastAPI()
REQUEST_COUNT = Counter("request_count", "Total request count")

@app.get("/")
def home():
    REQUEST_COUNT.inc()
    return {"message": "Hello from DevSecOps Dashboard 🚀"}

@app.get("/metrics")
def metrics():
    cpu_usage = psutil.cpu_percent()
    return Response(generate_latest(), media_type="text/plain")
