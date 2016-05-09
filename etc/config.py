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
cookie_str = '_ga=GA1.2.1285109683.1448638215; sd_userid=56791452780550806; sd_cookie_crttime=1452780550806; pgv_pvid=3428075355; o_cookie=474273647; pgv_pvi=2417586176; pgv_si=s4213506048; ptui_loginuin=1017545581; ptisp=cnc; RK=ZPPLNmxzYU; ptcz=a195cbe67a4b1f4d58b39b53970bb5bf7b47092e7d393847856c31cc76a1ceea; pt2gguin=o1017545581; uin=o1017545581; skey=@UqViXKred; p_uin=o1017545581; p_skey=VUsFuSlUjbiemfNdKyHatCYIglulGSbGDsYGDfVmmk8_; pt4_token=kBF2Bv1uNe8w3qGQ9AF0ZWvl93rtk9-7k1dGBL0AV8I_'

merge_top_url = 'http://buluo.qq.com/cgi-bin/bar/card/merge_top'
fans_url = 'http://buluo.qq.com/cgi-bin/bar/card/fans'
follow_list_url = 'http://buluo.qq.com/cgi-bin/bar/card/follow_list'

fans_page_num = 20
follow_list_page_num = 20

# this QQ follows many users
start_uins = ['280372450']
# this QQ follow many clans and has many followers
# start_uins = ['1182918']
