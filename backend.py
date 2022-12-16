import requests 
from requests.auth import HTTPDigestAuth
import time
import http.client
from queue import Queue, Empty
import asyncio
import websockets


q = Queue()


def run_requests():
    auth = HTTPDigestAuth("<camera_user>", "<camera_pass>")
    print(auth)

    print(requests.put("http://<camera_ip>/ISAPI/System/TwoWayAudio/channels/1/close", auth=auth))
    print(requests.put("http://<camera_ip>/ISAPI/System/TwoWayAudio/channels/1/open", auth=auth))

    conn = http.client.HTTPConnection("<camera_ip>")
    conn.putrequest('PUT', '/ISAPI/System/TwoWayAudio/channels/1/audioData')
    conn.putheader('Content-Type', 'application/octet-stream')
    conn.putheader('Connection', 'keep-alive')
    conn.putheader("Authorization", auth.build_digest_header("PUT", '/ISAPI/System/TwoWayAudio/channels/1/audioData'))
    conn.endheaders()

    conn.send(b'\r\n')

    while True:
        global q
        try:
            conn.send(q.get(block=True, timeout=2))
        except Empty:
            pass

    conn.send(b'\r\n')
    conn.send(b'\r\n')

    print(conn.getresponse())

    conn.close()

async def echo(websocket):
    async for message in websocket:
        print("msg")
        global q
        q.put(message)

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8765):
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, run_requests)
        await asyncio.Future()  # run forever

asyncio.run(main())
