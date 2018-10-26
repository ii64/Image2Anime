# -*- coding: utf-8 -*-
__author__   = "anysz, solury"
__version__  = "1.0.1"
__github__   = "https://github.com/anysz/Image2Anime"
__website__  = "https://github.co/solury/trace.moe"
from .main import Search
"""
    [Image2Anime-py] Search your Anime scene by Image! *YAY*
        Endpoint   - Solury (https://github.com/solury)
        Python API - Anysz  (https://github.com/anysz)

    Feels free to report code bug(s), i'll patch it as soon as possible
    or... Create Pull request :D 

    To start searching the scene you could do:
        By local file path:
            s = Image2Anime.Search('/path/to/source')
        By IO Text / Buffer
            f = open('/path/to/source', 'rb')
            s = Image2Anime.Search(f)
        By raw image data
            s = Image2Anime.Search(image_raw=b'raw binary image goes here')
        By image url
            s = Image2Anime.Search(url='http://to/image/url')
    and access the result in 
        s.result


"""