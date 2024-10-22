import os
import streamlink
import subprocess
import sys

username = os.environ.get('TF1_USER')
password = os.environ.get('TF1_PASSWORD')

url = 'https://www.tf1.fr/tf1/direct'

session = streamlink.Streamlink()

try:
    command = [
        "streamlink",
        "--tf1-email", username,
        "--tf1-password", password,
        url,
        "best"
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        m3u8_url = result.stdout.strip()
        print(m3u8_url)
    else:
        print(f"Error: {result.stderr.strip()}")
except Exception as e:
    print(f"An error occurred: {e}")
