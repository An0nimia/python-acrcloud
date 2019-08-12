#!/usr/bin/python3

import time
import hmac
import base64
import hashlib
import requests

bytes_to_read = 1000000

class ACRcloud:
	def __init__(self, config):
		self.key = config['key']
		self.secret = config['secret'].encode()
		self.host = config['host'] + "/v1/identify"

	def recognizer(self, audio):
		timestamp = str(time.time())

		example = base64.b64encode(
			open(
				audio, "rb"
			).read(bytes_to_read)
		)

		string_to_sign = (
			"%s\n%s\n%s\n%s\n%s\n%s" 
			% (
				"POST",
				"/v1/identify", 
				self.key, 
				"audio", 
				"1", 
				timestamp
			)
		).encode()

		sign = base64.b64encode(
			hmac.new(
				bytes(self.secret), 
				bytes(string_to_sign), 
				hashlib.sha1
			).digest()
		)

		data = {
			"access_key": self.key,
			"sample_bytes": bytes_to_read,
			"sample": example,
			"timestamp": timestamp,
			"signature": sign,
			"data_type": "audio",
			"signature_version": "1"
		}

		result = requests.post(
			self.host, data
		).json()

		return result