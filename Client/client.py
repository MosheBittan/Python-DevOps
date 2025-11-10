# client/client.py

import requests
import argparse
import os

# The URL of the server's scanning endpoint
SERVER_URL = "http://127.0.0.1:8000/scan/"

def send_file_for_scanning(file_path: str):
    """
    Sends a file to the server for scanning and prints the response.
    """
    if not os.path.exists(file_path):
        print(f"❌ Error: File not found at '{file_path}'")
        return

    # 'files' is a dictionary where the key ('file') must match the
    # parameter name in the FastAPI endpoint.
    # We open the file in binary read mode ('rb').
    with open(file_path, 'rb') as f:
        files = {'file': (os.path.basename(file_path), f)}
        
        print(f"🚀 Sending '{os.path.basename(file_path)}' to the server for scanning...")
        
        try:
            response = requests.post(SERVER_URL, files=files)
            
            # Check if the request was successful
            if response.status_code == 200:
                print("✅ Scan complete! Server response:")
                print(response.json())
            else:
                print(f"❌ Error: Server returned status code {response.status_code}")
                print("Response:", response.text)
        
        except requests.exceptions.ConnectionError as e:
            print(f"❌ Connection Error: Could not connect to the server at {SERVER_URL}.")
            print("Please ensure the server is running.")

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Send a file to the scanner API.")
    parser.add_argument("file", help="The path to the file you want to scan.")
    
    args = parser.parse_args()
    
    send_file_for_scanning(args.file)