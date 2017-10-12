import sys
from datetime import datetime
from analysis_fb.collector.api import json_request as jr

url = 'http://192.168.1.38:8088/mysite2/api/guestbook/list'


def success_fetch_guestbook_list(response):
    print(response)


def error_fetch_guestbook_list(e):
    print('%s : %s' % (e, datetime.now()), file=sys.stderr)

# jr.json_request(url=url, success=success_fetch_guestbook_list)
"""
jr.json_request(
    url=url,
    success=success_fetch_guestbook_list,
    error=error_fetch_guestbook_list)
"""

json_result = jr.json_request(url=url)
print(json_result)
