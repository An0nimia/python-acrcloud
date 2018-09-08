# acrcloud
This project has been created to detects the songs from an audio.
* ### OS Supported ###
    ![Linux Support](https://img.shields.io/badge/Linux-Support-brightgreen.svg)
    ![macOS Support](https://img.shields.io/badge/macOS-Support-brightgreen.svg)
    ![Windows Support](https://img.shields.io/badge/Windows-Support-brightgreen.svg)
* ### Installation ###
      pip3 install acrcloud
### Identify a song
    ```python
    config = {
              "key": YOUR ACCESS KEY,
              "secret": YOUR ACCESS SECRET,
              "host": YOUR HOST
    }
    import acrcloud
    audio = acrcloud.recognizer(config, file)
    ```