from typing import List

import requests
import bs4
import argparse

crawled_link_list = []
external = []


def extractor(soup: bs4.BeautifulSoup, host: str, base_path: str) -> List[str]:
    temp_list = []
    for link in soup.find_all('a', href=True):
        href = link["href"]
        if "https://" in href or "http://" in href:
            external.append(href)
            continue

        if href in temp_list:
            continue
        found_link = f"{host}{'' if base_path in href or base_path in host else base_path}{href}"
        temp_list.append(found_link)
    return temp_list


def crawl(link: str, host: str = None, base_path: str = None) -> List[str]:
    if host is None:
        host = link
    res = requests.get(link, allow_redirects=True)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    return extractor(soup, host, base_path)


def deep_crawl(new_link_list: List[str], host: str, base_path: str = None) -> None:
    global crawled_link_list
    if len(crawled_link_list) % 500 == 0:
        print(f"Crawled link list length is {len(crawled_link_list)}")
    for link in new_link_list:
        if link in crawled_link_list or link in external:
            continue
        new_list = [item for item in crawl(link, host, base_path) if item not in crawled_link_list and item not in new_link_list and item not in external]
        crawled_link_list = list(set(crawled_link_list + [link]))
        deep_crawl(new_list, host, base_path)


def validation(args: argparse.Namespace) -> None:
    if args.url is None:
        print("Please provide a URL with the -u arg")
        quit()

    if 'http' not in args.url:
        args.url = 'http://' + args.url

    if args.url[-1] == "/":
        args.url = args.url[:-1]

    if args.base_path and args.base_path[0] != "/":
        args.base_path = f"/{args.base_path}"

    if args.base_path and args.base_path[-1] == "/":
        args.base_path = args.base_path[:-1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='root url', dest='url')
    parser.add_argument('-b', '--base_path', help='base path', dest='base_path')
    parser.add_argument('-d', '--deepcrawl', help='crawl deeply', dest='deepcrawl', action='store_true')
    parser.add_argument('-e', '--external', help='extract external', dest='external', action='store_true')
    args = parser.parse_args()
    validation(args)
    global crawled_link_list

    host = f"{args.url}{args.base_path}"
    internal = crawl(host, args.url, args.base_path)
    crawled_link_list += [f"{host}/"]
    if args.deepcrawl:
        print('\nDEEPCRAWL ACTIVATED\n')
        deep_crawl(internal, args.url, args.base_path)
        internal = crawled_link_list

    if len(internal) == 0:
        print('\nNo Links Found\n')
    with open('link_crawler.txt', 'w') as f:
        f.write("\n".join(internal))

    if args.external:
        print('\nEXTERNAL LINKS : \n')
        if len(external) == 0:
            print('\nNo EXTERNAL Links Found\n')
        with open('external_link_crawler.txt', 'w') as f:
            f.write("\n".join(external))


if __name__ == "__main__":
    main()
