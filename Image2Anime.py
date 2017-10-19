import urllib, requests
class AniSearch(object):
  ## REQUIRED : urllib , requests
  def __init__(self, path):
    self.pic_path = path
    self.b64img = None
    self.season = None; self.anime = None
  def image_b64(self):
    with open(self.pic_path, 'rb') as img_file:
      encode_str = img_file.read()
      self.b64img = encode_str.encode('base64')
  def get_info(self, season, anime):
    js = self.get_info_(season,anime)
    ret_r = []
    for item in js:
      ret = {}
      ret['name_en'] = item['title_english']
      ret['name_jp'] = item['title_japanese']
      ret['genres']  = item['genres']
      ret['s_type']  = item['series_type']
      ret_r.append(ret)
    return ret_r
  def get_data(self, json):
    js = json;
    results = js['docs']
    ret = []
    for result in results:
      try:
        season = result['season']
        anime  = result['anime']
        file   = result['file']
        start_ = result['start']
        end___ = result['end']
        token  = result['token']
        token_ = result['tokenthumb']
        t__    = result['to']
        ncoded_anime = urllib.quote(anime) ; ncoded_file = urllib.quote(file) 
        url_r = 'https://whatanime.ga/' + season + '/' + ncoded_anime + '/' + ncoded_file
        url_r += '?start={0}&end={1}&token={2}'.format(start_,end___,token)
        url_t = 'https://whatanime.ga/thumbnail.php?season={0}&anime={1}&file={2}&t={3}&token={4}'.format(season,ncoded_anime,ncoded_file,t__,token_)
        ret.append({'video':url_r,'thumbnail':url_t,'anime_name':anime,'season':season})
      except Exception as e:
        pass
    return ret
  def get_info_(self, season, anime):
    header = {
      'Referer':'https://whatanime.ga/',
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
      'x-requested-with':'XMLHttpRequest',
    }
    url = 'https://whatanime.ga/info?season={0}&anime={1}'.format(season, urllib.quote(anime));
    r = requests.get(url, headers=header)
    return r.json()
  def post_image(self):
    try:
      self.image_b64()
    except Exception as e: raise Exception("Image cant be converted.");
    payload = "data=data:image/jpeg;base64," + self.b64img
    payload += '&filter=*&trial=4'
    header = {
      'Host':'whatanime.ga',
      'accept':'application/json, text/javascript, */*; q=0.01',
      'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
      'origin':'https://whatanime.ga',
      'referer':'https://whatanime.ga/',
      'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
      'x-requested-with':'XMLHttpRequest',
    }
    r = requests.post('https://whatanime.ga/search', data=payload, headers=header)
    if r.status_code == 200:
      return r.json()
    else:
      raise Exception("Post failed.")
