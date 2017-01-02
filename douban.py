# -*- coding: utf-8 -*-
import requests



def GetMovies(start,count,movie_type=u'热门'):
    
    #豆瓣上电影的评分的ＵＲＬ之一
    """
    doubanUrl = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=rank&page_limit='+str(count)+'&page_start='+str(start)
    
    doubanUrl = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=20&page_start=0'
    """
    doubanUrl = 'https://movie.douban.com/j/search_subjects'
    print('url:',doubanUrl)
    """
    参数的解释：
    'type=movie'+　#类型是电影
    '&tag=%E7%83%AD%E9%97%A8'+ #这个是电影的标签,应该是‘热门’这两个字，我们可以去百度查一下
    '&sort=rank'+#按照rank进行评分，这个rank应该就是用户的打分
    '&page_limit=20'+#每一页的限制查询数量，我想我们可以改，来改改试试。。。
    '&page_start=0'
    """
    
    payload = {'type': 'movie',
               'tag' : movie_type,
               'sort':'rank',
               'page_limit': count,
               'page_start':start
               }

#        r = requests.get('http://httpbin.org/get', params=payload)

    r = requests.get(doubanUrl,params=payload)
    print(r.url)
    data = r.json()
    
    print(u'查到了你想要的数据。。')
    fileMode = None
    if(start is 0):
        fileMode = "w"
    else:
        fileMode = "a+"
    if len(data) == 1:
        subjects = data['subjects']
        
        fileHandler = open('豆瓣'+movie_type+'电影.txt',fileMode)
        print('一共查询到:', len(subjects),'部电影。')
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
            str_line = '['+movie['title']+'] 评分:'+movie['rate']+' 详情地址：'+movie['url']+'\n'
            print(str_line)
            fileHandler.write(str_line)
            #这个时候基本上可以获得一些我们想要的信息了，但是，我并不满足。多获得一些电影试试
        fileHandler.close()
            
#我们将上面的代码封装成一个函数，用来获取我们想要的电影
#函数名GetMovies(参数1指定从多少位开始获得，参数2指定一次获得电影的数量)
#额。。。备份一下代码，如果想玩的话，一会儿自己可以下载一下自己本地跑一下
def main():
    #萌萌的查询200个数据试一下
    GetMovies(0,100,u'热门') #现在只是测试调用，test：OK!
    GetMovies(0,100,u'豆瓣高分') 
    #现在开始动态关联
    #GetMovies(1000,1000)
    
    #单纯了，好像没有查到40个数据
    #bug fixed！因为参数中加入了空格
    #备份一下代码
    #突然发现，做到这样基本就可以了。如果想看详细信息可以去豆瓣上看。
    #如果我再去获得每一个电影的概述，感觉意义不太大
    #来看看是不是可以获取前1000部电影
    
if __name__ == "__main__":
    main()