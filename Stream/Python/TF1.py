import os
import streamlink
import sys

username = os.environ.get('TF1_USER')
password = os.environ.get('TF1_PASSWORD')

url = 'https://www.tf1.fr/tf1/direct'

session = streamlink.Streamlink()

args = {
    'tf1-email': username,
    'tf1-password': password,
}

streams = session.streams(url, **args)

if streams:
    stream = streams.get('best')
    if stream:
        m3u8_url = stream.to_url()
        print(m3u8_url)
    else:
        print("No 'best' stream available.")
else:
    print("No streams found.")
