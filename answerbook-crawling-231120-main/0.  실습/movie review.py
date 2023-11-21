import requests as req
import json
import pandas as pd
from bs4 import BeautifulSoup as bs
def scrap():
    url = 'https://comment.daum.net/apis/v1/posts/149513756/comments?parentId=0&offset=10&limit=30&sort=RECOMMEND&isInitial=false&hasNext=true'
    res = req.get(url)
    movie_code = '149761585'
    count_url = f"https://comment.daum.net/apis/v1/comments/on/{movie_code}/flags"
    count_res = req.get(count_url)
    count_json = json.loads(count_res.text)
    print(f'1- count_json : {count_json}')
    total = int(int(count_json['count']) / 10)
    print(f'2- total : {total}')
    review_list = []
    for page in range(0, 2):
        url = f'https://comment.daum.net/apis/v1/posts/149761585/comments?parentId=0&offset=0&limit=10&sort=LATEST&isInitial=true&hasNext=true'
        res = req.get(url)
        ls = json.loads(res.text)
        print(f'3- list : {ls}')
        # 필요한 정보는 아이디, 별점, 리뷰코멘트
        # content rating displayName

        for i, _ in enumerate(ls):
            review = ls[i]["content"]
            user = ls[i]['user']["displayName"]
            rating = ls[i]["rating"]
            review_list.append([user, rating, review])

        df = pd.DataFrame(review_list, columns=["user", "rating", "review"])
        print(df)
        df.to_csv(f"./data/daum_movie_review.csv", index=False, encoding='utf-8-sig')




if __name__ == '__main__':
    scrap()