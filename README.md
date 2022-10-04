This is a fork of [dsuc](https://github.com/r3dxpl0it/Damn-Small-URL-Crawler)
## URL Crawler
Python crawler for extracting internal and external links from a URL. It can deep-crawl sites too.

### Usage 
##### Instalation
`git clone https://github.com/giovanni-caiazzo/py-url-crawler.git`
`cd` into directory and create a virtual env with the `requirements.txt`
##### Examples 
 - Normal Crawl
`python3 link_crawler.py -d -u http://testsite.com`
 - Normal Crawl with base path
`python3 link_crawler.py -d -u http://testsite.com -b /resources`
 - Show External Links 
`python3 link_crawler.py -d -u http://testsite.com -e` 
 - DeepCrawl 
`python3 link_crawler.py -d -u http://testsite.com`
