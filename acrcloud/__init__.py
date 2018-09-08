#!/usr/bin/python3
import os
import time
import hmac
import json
import base64
import hashlib
import requests
def recognizer(config, audio):
    timestamp = time.time()
    string_to_sign = "POST" + "\n" + "/v1/identify" + "\n" + config['key'] + "\n" + "audio" + "\n" + "1" + "\n" + str(timestamp)
    sign = base64.b64encode(hmac.new(bytes(config['secret'].encode()), bytes(string_to_sign.encode()), hashlib.sha1).digest())
    data = {"access_key": config['key'],
            "sample_bytes": os.path.getsize(audio),
            "sample": base64.b64encode(open(audio, "rb").read(1000000)),
            "timestamp": str(timestamp),
            "signature": sign,
            "data_type": "audio",
            "signature_version": "1"
    }
    return json.loads(requests.post(config['host'] + "/v1/identify", data).text)