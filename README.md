Image2Anime
----

[![Version 0.4](https://img.shields.io/badge/stable-1.5-brightgreen.svg "Version 0.4")](https://github.com/anysz/Image2Anime) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) [![Supported python versions: 2.7](https://img.shields.io/badge/python-2.7-green.svg "Supported python versions: 2.7")](https://www.python.org/download/releases/2.7/)

Refrence
----

- Based : [Solury Repo](https://github.com/soruly/whatanime.ga)
- WEB   : [The web](https://whatanime.ga/)

***The Endpoint isn't mine, I just make API***

Usage
----

 **In order you need to import urllib and requests**

     >>> import urllib, requests
    
 **First use**

     >>> ani_ = AniSearch('/path/to/file')

 **To submit picture (MUST)**

     >>> ret_ = ani_.post_image()

 **To get resource (Array)**
 
     >>> ret_res = ret_.get_data(ret_)

 **To get info spesific (Array)**

     >>> ret_ainfo = ret_.get_info(ret_res[0]['season'], res_res[0]['anime_name'])

 **QnA**

     Q : lib imported not found
     A : pip install PACKAGENAME


Screenshot
----------

![alt_tag](https://puu.sh/y202u/2c1c6009fa.png)

Special Thanks
----
[Solury](https://github.com/soruly)

Author
----

[Anysz](https://instagram.com/nugra.z) / [@Anysz](https://github.com/anysz)
