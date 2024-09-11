import uvicorn
from src.app import app
from src.config import settings

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.port)
