# server/main.py

import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException

# Create an instance of the FastAPI class
app = FastAPI()

# Define the directory where files will be saved temporarily
UPLOAD_DIRECTORY = "./uploads"
CLEAN_DIRECTORY = "./clean"

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

def scan_file(file_path: str) -> dict:
    """
    A mock scanning function.
    In a real-world scenario, this would integrate with a real scanning engine
    like ClamAV, or an API like VirusTotal.
    
    For this example, we'll just check if the file contains the string "MALWARE".
    This simulates finding a malicious signature.
    """
    print(f"🔬 Scanning file: {file_path}")
    try:
        with open(file_path, "r", encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Simple signature-based check
            if "MALWARE" in content:
                return {
                    "status": "infected",
                    "details": "Detected a simple 'MALWARE' signature."
                }
            else:
                return {
                    "status": "clean",
                    "details": "No malicious signatures found."
                }
    except Exception as e:
        print(f"Error scanning file: {e}")
        return {
            "status": "error",
            "details": str(e)
        }

@app.post("/scan/")
async def create_upload_file(file: UploadFile = File(...)):
    """
    This endpoint receives a file, saves it, scans it, and returns the result.
    """
    # Define the full path for the uploaded file
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    
    try:
        # Save the uploaded file to the server's filesystem
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Run our "scanner" on the file
        scan_result = scan_file(file_path)
        
        # if the file is infected - move to infected folder else to clean folder
        source_path = file_path
        print(scan_result["status"])
        if "infected" == scan_result["status"]:
            shutil.copy2(source_path, ".\infected")
        else:
            shutil.copy2(source_path, ".\clean")

        # Clean up the file after scanning
        os.remove(file_path)
        
        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "scan_result": scan_result
        }

    except Exception as e:
        # If anything goes wrong, return an HTTP error
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "File Scanner API is running. POST files to /scan/ to analyze them."}