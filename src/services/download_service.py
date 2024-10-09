import os
import tempfile
from fastapi import HTTPException
import yt_dlp
from src.core.logging_config import logger

class DownloadService:
    @staticmethod
    async def download_song(url: str) -> tuple:
        logger.info(f"Starting download for URL: {url}")
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s',
            'verbose': True,  # Add verbose output for debugging
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            prev_cwd = os.getcwd()
            os.chdir(temp_dir)
            logger.debug(f"Changed working directory to: {temp_dir}")

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    logger.debug("Extracting video info and downloading")
                    info = ydl.extract_info(url, download=True)
                    if 'title' not in info:
                        raise ValueError("Unable to extract video title")
                    filename = f"{info['title']}.mp3"
                
                if not os.path.exists(filename):
                    logger.error(f"File not found after download: {filename}")
                    raise FileNotFoundError(f"File not found: {filename}")
                
                file_path = os.path.join(temp_dir, filename)
                logger.info(f"Successfully downloaded: {filename}")
                return file_path, filename
            
            except yt_dlp.utils.DownloadError as e:
                logger.error(f"yt-dlp download error: {str(e)}", exc_info=True)
                raise HTTPException(status_code=400, detail=f"Download error: {str(e)}")
            except ValueError as e:
                logger.error(f"Value error: {str(e)}", exc_info=True)
                raise HTTPException(status_code=500, detail=f"Error extracting video info: {str(e)}")
            except FileNotFoundError as e:
                logger.error(f"File not found error: {str(e)}", exc_info=True)
                raise HTTPException(status_code=404, detail=str(e))
            except Exception as e:
                logger.error(f"An unexpected error occurred during download: {str(e)}", exc_info=True)
                raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
            
            finally:
                os.chdir(prev_cwd)
                logger.debug(f"Changed working directory back to: {prev_cwd}")