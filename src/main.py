from fastapi import FastAPI
from src.api.routes.v1 import endpoints as v1_endpoints
from src.config.settings import Settings

def create_application() -> FastAPI:
    settings = Settings()
    application = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)
    
    application.include_router(v1_endpoints.router, prefix="/api/v1")
    
    return application

app = create_application()