from fastapi import Depends
from src.services.download_service import DownloadService

def get_download_service() -> DownloadService:
    return DownloadService()