# -*- coding: utf-8 -*-
from . import config
from . import utils
from . import models

class Search(object):
    host = config.host
    def __init__(self, image_path_or_obj=None, image_raw=None, url=None, filter="", trial="0", debug=False, **kw):
        super(Search, self).__init__()
        self.debug = debug
        config.debug = debug
        if(url):
            if(debug): print('Using search by url')
            self.build_search_by_url(url, filter, trial, **kw)
        elif(image_path_or_obj):
            if(debug): print('Using search by local file')
            self.build_search_by_upload(image_path_or_obj, image_raw, filter, trial, **kw)
        else:
            raise AnimeException('Invalid parameter', 'args', 'No method to detect image source')
    def image_proxy(self, url):
        req = utils.sendGet(
            self.host['image'] + '/imgproxy', 
            headers={},
            params={'url': url})
        return req
    def build_search_by_url(self, url, **kw):
        braw = utils.downloadStream(url, 'last_anisearch', save=False, **kw)
        self.build_search_by_upload(image_raw=braw, **kw)
    def build_search_by_upload(self, image=None, image_raw=None, filter="", trial="0", **kw):
        b64i = utils.base64_image(image, image_raw)
        dpyl = b'data:image/jpeg;base64,' + b64i
        req  = utils.sendPost(
            self.host['main'] + '/search', 
            headers={},
            params={},
            data={
                "data": dpyl,
                "filter": filter,
                "trial": trial,
            })
        if(req.status_code != 200):
            raise models.AnimeException(req.status_code, req.headers, req.content)
        else:
            try:
                res_json = req.json()
            except Exception as e:
                raise models.AnimeException("Application", "Cant decode json response: search api", e)
            self.result = models.SearchResult()
            self.result.read(res_json)
    def __repr__(self):
        L = ['result=<...>']
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))