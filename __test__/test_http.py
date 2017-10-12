# 내 mysite3를 가져오는 crawler를 만들기
# 이 코드로는 ajax같은 동적frame은 데이터를 못가져옴

import sys
from urllib.request import Request, urlopen
from datetime import *

try:
    url = 'http://192.168.1.38:8088/mysite3/guestbook/ajax'
    request = Request(url)

    #찔러주기
    resp = urlopen(request)
    resp_body = resp.read().decode('utf-8')
    print(resp_body)
except Exception as e:
    # tuple사용 %s처음은 exception 메세지 e, %s두번째는 datetime넣기(윗줄에 import도 하기)
    print('%s : %s' % (e, datetime.now()), file=sys.stderr)





