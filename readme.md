##获得豆瓣各种分类的高分电影
https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=rank&page_limit=20&page_start=0

    #豆瓣ＵＲＬ分析
    doubanUrl = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=rank&page_limit='+str(count)+'&page_start='+str(start)
    
    doubanUrl = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=20&page_start=0'

    参数的解释：
    'type=movie'+　#类型是电影
    '&tag=%E7%83%AD%E9%97%A8'+ #这个是电影的标签,应该是‘热门’这两个字，我们可以去百度查一下
    '&sort=rank'+#按照rank进行评分，这个rank应该就是用户的打分
    '&page_limit=20'+#每一页的限制查询数量，我想我们可以改，来改改试试。。。
    '&page_start=0'


    这个ＡＰＩ是获取某一个指定ＩＤ的摘要信息，感觉没有需要的，但是放到这儿，万一哪天要用到呢
    https://movie.douban.com/j/subject_abstract?subject_id=25921812


已经可以初步下载一些电影的信息了

##欢迎下载本代码：
代码下载地址： https://github.com/pjkui/douyu_living_python/archive/master.zip

##第二步：添加函数
函数添加完毕了，大家可以继续下载。
##第三步，将评分数据写入到一个本地文件，方便自己随时看。
好了，废话不多说。直接第三步。
代码所在地址：https://github.com/pjkui/douyu_living_python

##第四步：获取豆瓣高分电影。
刚刚是豆瓣的热门电影
地址：https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=20&page_start=0
来，做这一步
 搞定了
##第五步：需求来了、、、、、
    用更优雅的方式去构建请求URL.
    还是做这一步吧，这一步做好后做第四步会更简单点儿
    搞定了

##第六步：上传一下代码
doing
以下几步还没做。。。
##第七步：清理一下代码。
写的太恶心了。要恶心吐了
已经清理
##第八步：添加多些查询。
 添加了：热门  最新  经典  可播放  豆瓣高分  冷门佳片  华语  欧美  韩国 日本  动作  喜剧  爱情  科幻  悬疑  恐怖  动画

 ##第九步 基本完成了