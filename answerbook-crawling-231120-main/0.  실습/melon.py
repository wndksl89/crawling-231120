class Melon:
    def __init__(self):
        self.domain:'https://www.melon.com/chart/index.htm?dayTime='
        self.url = ''
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.class_name = []
        self.title_ls = []
        self.artist_ls = []
        self.dict = {}
        self.df = None

        def get_url(self)

            from bs4 import BeautifulSoup
            import requests

            class Melon(object):
                url = 'https://www.melon.com/chart/index.htm?dayTime='
                headers = {'User-Agent': 'Mozilla/5.0'}
                class_name = []

                def set_url(self, time):
                    self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

                def get_ranking(self):
                    soup = BeautifulSoup(self.url, 'lxml')
                    print('------- 제목 --------')
                    ls = soup.find_all("div", {"class": self.class_name[0]})
                    for i in ls:
                        print(f' {i.find("a").text}')
                    print('------ 가수 --------')
                    ls = soup.find_all("div", {"class": self.class_name[1]})
                    for i in ls:
                        print(f' {i.find("a").text}')