from urllib.parse import urlencode

BASE_URL_FB_API = 'https://graph.facebook.com/v2.10'


def fb_gen_url(base=BASE_URL_FB_API, node='', **params):
    return '%s/%s/?%s' % (base, node, urlencode(params))


def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(
        node=pagename + "/posts",
        fields = 'id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)')
