from fastapi import FastAPI

app = FastAPI(title="CodeDNA Inventory API")


@app.get("/health")
def health():
    return {"status": "ok", "service": "inventory-api"}
