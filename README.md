This is a fork of [dsuc](https://github.com/r3dxpl0it/Damn-Small-URL-Crawler)
## URL Crawler
Python Crawler for Extracting Internal and External Links from a link. It can deep-crawl sites too.

### Usage 
##### Instalation
`git clone https://github.com/r3dxpl0it/Damn_Small_URL_Crawler && cd Damn_Small_URL_Crawler && pip install -r	requirements.txt`
##### Examples 
 - Normal Crawl
`python3 dsuc.py -u http://testsite.com`
 - Show Fuzzable Links 
`python3 dsuc.py -u http://testsite.com -f` 
 - Show External Links 
`python3 dsuc.py -u http://testsite.com -e` 
 - DeepCrawl and Show Fuzzable Links 
`python3 dsuc.py -u -d http://testsite.com -f`
