from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from src.services.download_service import DownloadService
from src.core.logging_config import logger

router = APIRouter()

@router.get("/download-song")
async def download_song(url: str, download_service: DownloadService = Depends()):
    logger.info(f"Download song endpoint accessed for URL: {url}")
    try:
        file_path, filename = await download_service.download_song(url)
        logger.info(f"Successfully processed download request for: {filename}")
        return FileResponse(file_path, media_type='audio/mpeg', filename=filename)
    except HTTPException as e:
        logger.error(f"HTTP exception occurred: {str(e)}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error occurred: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
