# -*- coding: utf-8 -*-
import requests

"""
函数名GetMovies(参数1指定从多少位开始获得数据，参数2指定一次请求获得电影的数量)
好业余的注释，也只能这样了。。。。
"""
def GetMovies(start,count,movie_type=u'热门'):

    doubanUrl = 'https://movie.douban.com/j/search_subjects'
    payload = {'type': 'movie',# query type
               'tag' : movie_type, #movie type
               'sort':'rank',#你懂的，按照评分排序
               'page_limit': count,
               'page_start':start
               }
    #写demo的人都比较ＮＢ，所以就是不加try catch.建议还是加一下
    r = requests.get(doubanUrl,params=payload)
    #print(r.url)#如果不确定这个url构建的是否正确，你就打开这句话，让他输出。。。
    data = r.json()
    
    print(u'竟然没有崩溃的情况下就查到了你想要的数据，你是不是很开森。。')
    
    #下面的代码是进行文件的处理，第一次创建文件，第二次进行文件追加
    #虽然不优雅，但是可以用。。。
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
        #每一个电影格式的说明
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
        #关闭文件处理句柄，句柄就是。。。神经病啊，我是随口说的而已，其实就是打开的文件，win下的程序猿莫名的会说句柄
        fileHandler.close()

#额。。。备份一下代码，如果想玩的话，一会儿自己可以下载一下自己本地跑一下
def main():
    #萌萌的查询200个数据试一下
    GetMovies(0,200,u'热门') #查询豆瓣热门电影，test：OK!
    GetMovies(0,200,u'豆瓣高分')#查询豆瓣高分电影
    GetMovies(0,200,u'科幻')#这个我还真没试过，先跑跑程序再说，反正电脑不会蓝屏。。
    GetMovies(0,200,u'悬疑')
    GetMovies(0,200,u'喜剧')
    #GetMovies(0,200,u'热门')
    GetMovies(0,200,u'最新')
    GetMovies(0,200,u'经典')
    GetMovies(0,200,u'可播放')
    #GetMovies(0,200,u'豆瓣高分')
    GetMovies(0,200,u'冷门佳片')
    GetMovies(0,200,u'华语')
    GetMovies(0,200,u'欧美')
    GetMovies(0,200,u'韩国')
    GetMovies(0,200,u'日本')
    GetMovies(0,200,u'动作')
    GetMovies(0,200,u'喜剧')
    GetMovies(0,200,u'爱情')
    #GetMovies(0,200,u'科幻')
    GetMovies(0,200,u'悬疑')
    GetMovies(0,200,u'恐怖')
    GetMovies(0,200,u'文艺')
    
    
    
    
    
    
    
    
    
    
    
    
    #以下是胡说八道，反正说的都已经不是很重要了。。。
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