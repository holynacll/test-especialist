from fastapi import UploadFile
from src.config import settings


async def upload_file(file: UploadFile):
    file_path = settings.static_dir / file.filename
    # Salva o arquivo original temporariamente
    with file_path.open(mode="wb") as f:
        f.write(await file.read())
    return file_path


def text_parser(text: str):
    lines = text.strip().split('\n')
    data = {}
    for line in lines:
        key, value = line.split(': ', 1)
        data[key] = value
    return data
