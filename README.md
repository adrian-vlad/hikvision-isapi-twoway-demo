# hikvision-isapi-twoway-demo
This is a simple demo showing how to talk back to a hikvision camera that has speaker using the ISAPI protocol.

## Prepare
1. need python3 installed where `backend.py` is going to be run
2. modify `backend.py` and replace with the appropriate values the following: `<camera_ip>`, `<camera_user>`, `<camera_pass>`
3. modify `index.html` and replace with the IP of the machine that is going to run the following: `<backend_address>` 


## Run
1. run `python3 backend.py`
2. open `index.html` in your browser
3. click `Allow` to use microphone
4. press `start audio` and speak
5. you should hear the camera playing your voice on the speaker
