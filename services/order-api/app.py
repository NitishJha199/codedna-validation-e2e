from fastapi import FastAPI

app = FastAPI(title="CodeDNA Order API")


@app.get("/health")
def health():
    return {"status": "ok", "service": "order-api"}
