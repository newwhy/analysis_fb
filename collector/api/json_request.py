import sys
from urllib.request import Request, urlopen
from datetime import *
import json


def json_request(
        url='',
        encoding='utf-8',
        success=None,
        error=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        # 여기 url에 크롤링할 url따오기 url = 'http://192.168.1.38:8088/mysite3/api/guestbook/list'
        request = Request(url)
        resp = urlopen(request)

        resp_body = resp.read().decode(encoding)
        json_result = json.loads(resp_body)

        if callable(success) is False:# 만약 함수를 안넣었을시=False 면
            return json_result

        success(json_result)

    except Exception as e:
        callable(error) and error(e)


#    except Exception as e:
#        print('%s : %s' % (e, datetime.now()), file=sys.stderr)


