import sys
import requests
from bs4 import BeautifulSoup

# --> todas as URLS que quer fazer o crowl
TO_CRAWL = []
CRAWLED = set()


# --> função request que trata melhor o request vs response vs erro (ao inves de simplesmente usar requests.get)
def request(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    try:
        response = requests.get(url, headers=header)
        return response.text
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        pass


def get_links(html):
    links = []
    try:
        soup = BeautifulSoup(html, "html.parser")
        tags_a = soup.find_all("a", href=True)

        for tag in tags_a:
            link = tag["href"]
            if link.startswith("http"):
                links.append(link)

        return links
    except:
        pass


def crawl():
    while 1:
        if TO_CRAWL:
            url = TO_CRAWL.pop()

            html = request(url)
            if html:
                links = get_links(html)
                if links:
                    for link in links:
                        if link not in CRAWLED and link not in TO_CRAWL:
                            TO_CRAWL.append(link)

                print(f"Crawling {url}")
                CRAWLED.add(url)
            else:
                CRAWLED.add(url)
        else:
            print("Done")
            break


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        TO_CRAWL.append(url)

        crawl()
    except:
        print("USAGE: python3 web-crawler.py https://www.site.com")
