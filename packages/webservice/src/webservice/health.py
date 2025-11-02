from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "ok"}
