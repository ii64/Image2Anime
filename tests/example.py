# -*- coding: utf-8 -*-
import os, sys
try:
	import Image2Anime
except:
	print('Image2Anime is not installed yet :(')
	os._exit(0)

if __name__ == '__main__':
	s = Image2Anime.Search(r'test.jpg')
	first_result = s.result.scenes[0]
	print('First result:', first_result)
	print()
	print('All results:', s.result)
