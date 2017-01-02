# -*- coding: utf-8 -*-
import requests


#豆瓣上电影的评分的ＵＲＬ之一
doubanUrl = 'https://movie.douban.com/j/search_subjects?\
type=movie\
&tag=%E7%83%AD%E9%97%A8\
&sort=rank\
&page_limit=20\
&page_start=0'


"""
参数的解释：
'type=movie'+　#类型是电影
'&tag=%E7%83%AD%E9%97%A8'+ #这个是电影的标签,应该是‘热门’这两个字，我们可以去百度查一下
'&sort=rank'+#按照rank进行评分，这个rank应该就是用户的打分
'&page_limit=20'+#每一页的限制查询数量，我想我们可以改，来改改试试。。。
'&page_start=0'
"""

r = requests.get(doubanUrl)
data = r.json()
print('data length:',len(data))
if len(data) == 1:
    subjects = data['subjects']
    print('subjects length(查询到的电影数量：):', len(subjects))
    #开始解析查询到的电影信息
    """
    {'cover': 'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2315672647.jpg',
    cover 电影的封面 
    'cover_x': 1418, 不知道什么鬼
     'cover_y': 2005, 也不知道什么鬼
     'id': '25662329', 电影的id
     'is_beetle_subject': False,不懂
     'is_new': False,不是最新
     'playable': True,是否可以播放
     'rate': '9.2',
     'title': '疯狂动物城',
     'url': 'https://movie.douban.com/subject/25662329/'}
     豆瓣上具体的详细介绍的地址
     """
    for movie in subjects:
        print(movie['title'],'评分:',movie['rate'])
        #这个时候基本上可以获得一些我们想要的信息了，但是，我并不满足。多获得一些电影试试
        
        
#我们将上面的代码封装成一个函数，用来获取我们想要的电影
#函数名GetMovies(参数1指定一次获得电影的数量，参数2指定从多少位开始获得)
#额。。。备份一下代码，如果想玩的话，一会儿自己可以下载一下自己本地跑一下

