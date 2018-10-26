# -*- coding: utf-8 -*-
# Server API behind cloudflare - enforce https
host = {
	'main' : 'https://trace.moe',
	'image': 'https://image.trace.moe', #/imgproxy?url=https://.....
}
headers = {
	'origin': host['main'],
	'referer': host['main'] + '/',
	'user-agent': 'Image2Anime-Py AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
	'x-requested-with': 'XMLHttpRequest',
}
verify_http_request = False
debug = False