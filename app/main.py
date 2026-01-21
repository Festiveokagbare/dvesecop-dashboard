from fastapi import FastAPI, Request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI()

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

@app.middleware("http")
async def count_requests(request: Request, call_next):
    response = await call_next(request)
    REQUEST_COUNT.labels(request.method, request.url.path).inc()
    return response

@app.get("/")
def read_root():
    return {"message": "DevSecOps Dashboard Running"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
