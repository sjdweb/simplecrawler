import urllib2
from bs4 import BeautifulSoup


class Spyder(object):
    def __init__(self, base_url):
        self.to_crawl = []
        self.crawled = []
        self.results = []
        self.base_url = base_url

    def run(self):
        self.add_url('/')
        while 1:
            try:
                crawling = self.to_crawl.pop()
            except IndexError:
                return self.results

            try:
                result = self.parse_page(crawling)
            except:
                continue

            self.crawled.append(crawling)

            page_done = {
                'url': crawling,
                'static_assets': result['static_files']
            }
            self.results.append(page_done)

            for link in result['links']:
                self.add_url(link)

    def get_url(self, url):
        try:
            result = urllib2.urlopen(url).read()
            return BeautifulSoup(result)
        except Exception as e:
            print e.message
            return None

    def parse_page(self, url):
        soup = self.get_url(url)
        if soup is None:
            return None

        suitable_links = []
        static_files = []
        a_elements = soup.select("a")
        css_tags = soup.select("link[rel=stylesheet]")
        script_tags = soup.select("script[type=text/javascript]")
        img_tags = soup.select("img")

        for link in a_elements:
            if str.startswith(link['href'], '/'):
                suitable_links.append(link['href'])
        for css_tag in css_tags:
            try:
                static_files.append(css_tag['href'])
            except KeyError:
                pass
        for script_tag in script_tags:
            try:
                static_files.append(script_tag['src'])
            except KeyError:
                pass
        for img_tag in img_tags:
            try:
                if img_tag['src'] not in static_files:
                    static_files.append(img_tag['src'])
            except KeyError:
                pass

        return {'links': suitable_links, 'static_files': static_files}

    def add_url(self, url):
        excluded_files = ['.pdf', '.png', '.jpg']
        for excluded_file in excluded_files:
            if str.endswith(url, excluded_file):
                return None

        if not str.startswith(url, 'http://'):
            url = self.base_url + url
        if url not in self.crawled:
            if url not in self.to_crawl:
                self.to_crawl.append(url)