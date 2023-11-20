import pandas as pd
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

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = input('0-exit, 1-input time, 2-output')
            if menu == '0':
                break
            elif menu == '1':
                melon.set_url(input('20231120'))  # '2023111711'
            elif menu == '2':
                melon.class_name.append('ellipsis rank01')
                melon.class_name.append('ellipsis rank02')
                melon.get_ranking()
            else:
                print('Wrong number')
                continue

    def insert_dict(self):
        for i, j in enumerate(self.title_ls):
            self.dict[j] = self.artist_ls[i]

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print('딕셔너리 데이터를 데이터프레임에 이전 했습니다.')
        print(self.df)

    def df_to_csv(self):
        path = './data/bugs.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')
        print('데이터가 CSV 파일에 저장되었습니다.')


if __name__ == '__main__':
    Melon.main()
