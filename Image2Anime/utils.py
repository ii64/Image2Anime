# -*- coding: utf-8 -*-
from . import config
import base64
import urllib3
import requests

headers = config.headers
s = requests.session()
def urlencode(r):
	if(isinstance(r, (dict))):
		rs = (urllib3.request).urlencode(r)
		return rs
	else:
		rs = (urllib3.request).urlencode({'EX': r})
		return rs[3:]
def base64_image(image_path_or_obj, image_raw=None):
	if(image_raw):
		if(isinstance(image_raw, (str))):
			image_raw = image_raw.encode()
		return base64.b64encode(image_raw)
	elif getattr(type(image_path_or_obj), '__name__') in ('BufferedReader', 'TextIOWrapper'):
		return base64.b64encode(image_path_or_obj.read())
	else:
		with open(image_path_or_obj, 'rb') as f:
			return base64.b64encode(f.read())
def sendPost(uri, **kw):
	global s, headers
	kw['headers'] = {**headers, **kw.get('headers',{})}
	kw['verify'] = config.verify_http_request
	if(config.debug): print('sendPost', uri)
	return s.post(uri, **kw)
def sendGet(uri, **kw):
	global s, headers
	kw['headers'] = {**headers, **kw.get('headers',{})}
	kw['verify'] = config.verify_http_request
	if(config.debug): print('sendGet', uri)
	return s.get(uri, **kw)

def downloadStream(url, path='temp_downloaded',*, save=True, timeout=120, **kw):
	h = {**headers, **kw.get('headers',{})}
	try:
		print('Downloading %r'%(url))
		b = b''
		with sendGet(url, headers=h, timeout=timeout, **kw) as fd:
			contentlength = int(fd.headers.get('Content-Length', fd.headers.get('content-length',0)))
			print(f'File Size: {contentlength/1024/1024} MB')
			while True:
				sd = fd.raw.read(1024 * 10)
				if len(sd) != 0:
					b += sd
					sys.stdout.write(f'{len(b)}/{contentlength} [{str(len(b)/contentlength * 100)[:5]}%]')
					sys.stdout.flush()
				else:
					break
		print('Download finished.')
		if(save):
			with open(path, 'wb') as fw:
				fw.write(b)
		else:
			return b
	except Exception as e:
		print(e)