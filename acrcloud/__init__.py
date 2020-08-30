#!/usr/bin/python3

from time import time
from hashlib import sha1
from requests import post
from base64 import b64encode
from hmac import new as hmac_new

bytes_to_read = 1000000

class ACRcloud:
	def __init__(self, config):
		self.key = config['key']
		self.secret = config['secret'].encode()
		self.host = "%s/v1/identify" % config['host']

	def recognizer(self, audio):
		timestamp = str(
			time()
		)

		f = open(audio, "rb")

		example = b64encode(
			f.read(bytes_to_read)
		)

		f.close()

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

		sign = b64encode(
			hmac_new(
				bytes(self.secret), 
				bytes(string_to_sign),
				sha1
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

		result = post(self.host, data).json()
		return result