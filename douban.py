# -*- coding: utf-8 -*-
import requests
import codecs
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
        
        fileHandler = codecs.open('豆瓣'+movie_type+'电影.txt',fileMode,"utf-8")
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
    # #萌萌的查询200个数据试一下
    # GetMovies(0,200,u'热门') #查询豆瓣热门电影，test：OK!
    # GetMovies(0,200,u'豆瓣高分')#查询豆瓣高分电影
    # GetMovies(0,200,u'科幻')#这个我还真没试过，先跑跑程序再说，反正电脑不会蓝屏。。
    # GetMovies(0,200,u'悬疑')
    # GetMovies(0,200,u'喜剧')
    # #GetMovies(0,200,u'热门')
    # GetMovies(0,200,u'最新')
    # GetMovies(0,200,u'经典')
    # GetMovies(0,200,u'可播放')
    # #GetMovies(0,200,u'豆瓣高分')
    # GetMovies(0,200,u'冷门佳片')
    # GetMovies(0,200,u'华语')
    # GetMovies(0,200,u'欧美')
    # GetMovies(0,200,u'韩国')
    # GetMovies(0,200,u'日本')
    # GetMovies(0,200,u'动作')
    # GetMovies(0,200,u'喜剧')
    # GetMovies(0,200,u'爱情')
    # #GetMovies(0,200,u'科幻')
    # GetMovies(0,200,u'悬疑')
    # GetMovies(0,200,u'恐怖')
    # GetMovies(0,200,u'文艺')
    # GetMovies(0,200,u'动画')
    # GetMovies(0,200,u'纪录片')
    
    GetMovies(0,200,u'爱情')
    GetMovies(0,200,u'喜剧')
    GetMovies(0,200,u'动画')
    GetMovies(0,200,u'剧情')
    GetMovies(0,200,u'科幻')
    GetMovies(0,200,u'动作')
    GetMovies(0,200,u'经典')
    GetMovies(0,200,u'悬疑')
    GetMovies(0,200,u'青春')
    GetMovies(0,200,u'犯罪')
    GetMovies(0,200,u'惊悚')
    GetMovies(0,200,u'文艺')
    GetMovies(0,200,u'搞笑')
    GetMovies(0,200,u'纪录片')
    GetMovies(0,200,u'励志')
    GetMovies(0,200,u'恐怖')
    GetMovies(0,200,u'战争')
    GetMovies(0,200,u'短片')
    GetMovies(0,200,u'黑色幽默')
    GetMovies(0,200,u'魔幻')
    GetMovies(0,200,u'传记')
    GetMovies(0,200,u'情色')
    GetMovies(0,200,u'感人')
    GetMovies(0,200,u'暴力')
    GetMovies(0,200,u'动画短片')
    GetMovies(0,200,u'家庭')
    GetMovies(0,200,u'音乐')
    GetMovies(0,200,u'童年')
    GetMovies(0,200,u'浪漫')
    GetMovies(0,200,u'黑帮')
    GetMovies(0,200,u'女性')
    GetMovies(0,200,u'同志')
    GetMovies(0,200,u'史诗')
    GetMovies(0,200,u'烂片')
    GetMovies(0,200,u'童话')
    GetMovies(0,200,u'cult')
    GetMovies(0,200,u'美国')
    GetMovies(0,200,u'日本')
    GetMovies(0,200,u'香港')
    GetMovies(0,200,u'英国')
    GetMovies(0,200,u'中国')
    GetMovies(0,200,u'法国')
    GetMovies(0,200,u'韩国')
    GetMovies(0,200,u'台湾')
    GetMovies(0,200,u'中国大陆')
    GetMovies(0,200,u'德国')
    GetMovies(0,200,u'意大利')
    GetMovies(0,200,u'印度')
    GetMovies(0,200,u'内地')
    GetMovies(0,200,u'泰国')
    GetMovies(0,200,u'西班牙')
    GetMovies(0,200,u'欧洲')
    GetMovies(0,200,u'加拿大')
    GetMovies(0,200,u'澳大利亚')
    GetMovies(0,200,u'俄罗斯')
    GetMovies(0,200,u'伊朗')
    GetMovies(0,200,u'爱尔兰')
    GetMovies(0,200,u'瑞典')
    GetMovies(0,200,u'巴西')
    GetMovies(0,200,u'丹麦')
    GetMovies(0,200,u'波兰')
    GetMovies(0,200,u'捷克')
    GetMovies(0,200,u'阿根廷')
    GetMovies(0,200,u'比利时')
    GetMovies(0,200,u'墨西哥')
    GetMovies(0,200,u'新西兰')
    GetMovies(0,200,u'荷兰')
    GetMovies(0,200,u'奥地利')
    GetMovies(0,200,u'土耳其')
    GetMovies(0,200,u'匈牙利')
    GetMovies(0,200,u'以色列')
    GetMovies(0,200,u'新加坡')
    GetMovies(0,200,u'周星驰')
    GetMovies(0,200,u'宫崎骏')
    GetMovies(0,200,u'王家卫')
    GetMovies(0,200,u'JohnnyDepp')
    GetMovies(0,200,u'岩井俊二')
    GetMovies(0,200,u'梁朝伟')
    GetMovies(0,200,u'张艺谋')
    GetMovies(0,200,u'尼古拉斯·凯奇')
    GetMovies(0,200,u'冯小刚')
    GetMovies(0,200,u'斯皮尔伯格')
    GetMovies(0,200,u'成龙')
    GetMovies(0,200,u'刘德华')
    GetMovies(0,200,u'张国荣')
    GetMovies(0,200,u'姜文')
    GetMovies(0,200,u'杜琪峰')
    GetMovies(0,200,u'李连杰')
    GetMovies(0,200,u'徐克')
    GetMovies(0,200,u'李安')
    GetMovies(0,200,u'TimBurton')
    GetMovies(0,200,u'桂纶镁')
    GetMovies(0,200,u'周迅')
    GetMovies(0,200,u'周润发')
    GetMovies(0,200,u'金城武')
    GetMovies(0,200,u'刘青云')
    GetMovies(0,200,u'舒淇')
    GetMovies(0,200,u'王晶')
    GetMovies(0,200,u'希区柯克')
    GetMovies(0,200,u'新海诚')
    GetMovies(0,200,u'吴彦祖')
    GetMovies(0,200,u'汤姆·汉克斯')
    GetMovies(0,200,u'徐静蕾')
    GetMovies(0,200,u'奥黛丽·赫本')
    GetMovies(0,200,u'AnneHathaway')
    GetMovies(0,200,u'JimCarrey')
    GetMovies(0,200,u'科恩兄弟')
    GetMovies(0,200,u'贾樟柯')
    GetMovies(0,200,u'2015')
    GetMovies(0,200,u'2013')
    GetMovies(0,200,u'2014')
    GetMovies(0,200,u'2011')
    GetMovies(0,200,u'2012')
    GetMovies(0,200,u'2016')
    GetMovies(0,200,u'2010')
    GetMovies(0,200,u'2009')
    GetMovies(0,200,u'2008')
    GetMovies(0,200,u'2007')
    GetMovies(0,200,u'2006')
    GetMovies(0,200,u'2004')
    GetMovies(0,200,u'2005')
    GetMovies(0,200,u'2003')
    GetMovies(0,200,u'2001')
    GetMovies(0,200,u'2002')
    GetMovies(0,200,u'1994')
    GetMovies(0,200,u'2000')
    GetMovies(0,200,u'1997')
    GetMovies(0,200,u'1999')
    GetMovies(0,200,u'1998')
    GetMovies(0,200,u'1995')
    GetMovies(0,200,u'1996')
    GetMovies(0,200,u'1993')
    GetMovies(0,200,u'1992')
    GetMovies(0,200,u'1990')
    GetMovies(0,200,u'1991')
    GetMovies(0,200,u'1988')
    
    
    
    
    
    
    
    
    
    
    
    
    
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