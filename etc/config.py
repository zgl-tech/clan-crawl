#  coding: utf-8

DEBUG = False

mongodb_config = {
    'host': 'localhost',
    'port': 27017,
}
mongodb_dbname = 'clan_crawl'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/47.0.2526.80 Safari/537.36',
           'Referer': 'http://buluo.qq.com/mobile/personal.html'}
cookie_str = '_ga=GA1.2.1285109683.1448638215; sd_userid=56791452780550806; sd_cookie_crttime=1452780550806; RK=wEvSm1nDda; luin=o1017545581; lskey=00010000d77258871cc689d02a5762ef02217563405f1af37ed0ab15bf8b6e1d9b60ae40319570cb15d1507e; pgv_pvi=538806272; pgv_info=ssid=s4017903272; pgv_pvid=3428075355; o_cookie=1017545581; uid=318777340; pgv_si=s3396374528; ptisp=ctc; ptcz=a195cbe67a4b1f4d58b39b53970bb5bf7b47092e7d393847856c31cc76a1ceea; pt2gguin=o1017545581; p_uin=o1017545581; p_skey=F4wt0ekQRN-v3hiOhpSlZ9i6c*kKt4npk9rAfyWbSM4_; pt4_token=boN0gH5y5ODC1q*3t5cvB1HShI2vzT1EKUsqHItsmb0__ga=GA1.2.1285109683.1448638215; sd_userid=56791452780550806; sd_cookie_crttime=1452780550806; RK=wEvSm1nDda; luin=o1017545581; lskey=00010000d77258871cc689d02a5762ef02217563405f1af37ed0ab15bf8b6e1d9b60ae40319570cb15d1507e; pgv_pvi=538806272; pgv_info=ssid=s4017903272; pgv_pvid=3428075355; o_cookie=1017545581; uid=318777340; pgv_si=s3396374528; ptisp=ctc; ptcz=a195cbe67a4b1f4d58b39b53970bb5bf7b47092e7d393847856c31cc76a1ceea; pt2gguin=o1017545581; p_uin=o1017545581; p_skey=F4wt0ekQRN-v3hiOhpSlZ9i6c*kKt4npk9rAfyWbSM4_; pt4_token=boN0gH5y5ODC1q*3t5cvB1HShI2vzT1EKUsqHItsmb0_'
merge_top_url = 'http://buluo.qq.com/cgi-bin/bar/card/merge_top'
fans_url = 'http://buluo.qq.com/cgi-bin/bar/card/fans'

fans_page_num = 20

start_uins = ['969669230']
