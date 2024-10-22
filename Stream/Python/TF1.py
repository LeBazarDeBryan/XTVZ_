import os
import streamlink

username = os.environ.get('TF1_USER')
password = os.environ.get('TF1_PASSWORD')

url = 'https://www.tf1.fr/direct'

session = streamlink.Streamlink()
session.set_plugin_option('tf1', 'email', email)
session.set_plugin_option('tf1', 'password', password)

streams = session.streams(url)

if streams:
    stream = streams.get('best')
    if stream:
        m3u8_url = stream.to_url()
        print(m3u8_url)
    else:
        print("No 'best' stream available.")
else:
    print("No streams found.")
