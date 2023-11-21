import requests as req
import json
import pandas as pd
from bs4 import BeautifulSoup as bs

class DaumMovie:
    def __init__(self):
        self.url = ''

    def set_url(self,url):
        self.url = url

    def get_reviews(self):
        res = req.get(self.url)
        movie_code = '163819360'
        count_url = f"https://comment.daum.net/apis/v1/comments/on/{movie_code}/flags"
        count_res = req.get(count_url)
        count_json = json.loads(count_res.text)
        print(f'1- count_json : {count_json}')
        return count_json


if __name__ == '__main__':
    d = DaumMovie()
    # u = input('영화 url을 입력하시오')
    u = 'https://comment.daum.net/apis/v1/posts/163819360/comments?parentId=0&offset=0&limit=10&sort=LATEST&isInitial=true&hasNext=true'
    d.set_url(u)
    u2 = d.get_reviews()
    print(f'1- 리뷰수 : {count_json}')gi