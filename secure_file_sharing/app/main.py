from fastapi import FastAPI
from app.routers import auth, files

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(files.router, prefix="/files", tags=["files"])

@app.on_event("startup")
def on_startup():
    from app.database import engine
    from app.models import Base
    Base.metadata.create_all(bind=engine)
