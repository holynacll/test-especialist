from typing import Annotated

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from src.config import settings
from src.utils import upload_file
from src.documentation import analyze_document


static_path = settings.base_dir / "static"
if not static_path.exists():
    static_path.mkdir(parents=True, exist_ok=True)


app = FastAPI()

app.mount(settings.static_dir.as_posix(), StaticFiles(directory="static"), name="static")


@app.post("/analyze/software/documentation")
async def analyze_software_documentation(
    file: Annotated[UploadFile, File(description="A software documentation pdf file")]
):
    file_path = await upload_file(file)
    pdf_document_resulted = await analyze_documentation(file_path)
    # return JSONResponse(content=text_parsed)
