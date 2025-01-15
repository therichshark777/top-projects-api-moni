from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .routers import projectRoute

app = FastAPI()
app.include_router(projectRoute.router, prefix="/projects", tags=["Projects"])

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")