# acrcloud
This project has been created to detects the songs from an audio.
* ### OS Supported ###
    ![Linux Support](https://img.shields.io/badge/Linux-Support-brightgreen.svg)
    ![macOS Support](https://img.shields.io/badge/macOS-Support-brightgreen.svg)
    ![Windows Support](https://img.shields.io/badge/Windows-Support-brightgreen.svg)
* ### Important ###
    For get the access key, access secret and host watch (https://www.acrcloud.com/docs/acrcloud/)    
* ### Installation ###
      pip3 install acrcloud
### Identify a song
Identify a song by an audio
```python
import acrcloud
config = {
          "key": YOUR ACCESS KEY,
          "secret": YOUR ACCESS SECRET,
          "host": YOUR HOST
}
file = "audio.mp3"
audio = acrcloud.recognizer(config, file)
```
# Disclaimer
I am not the owner of ACRCloud