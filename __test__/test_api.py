from analysis_fb.collector.api import api

url = api.fb_gen_url(pagename='jtbcnews', a=1, b=2, no=3, token='321321')
print(url)
