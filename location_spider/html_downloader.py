import urllib2


class HtmlDownloader(object):

    def download(self, code):
        url = 'http://opendata.baidu.com/api.php?query=' + str(code)
        url += '0000&co=&resource_id=6004&t=1334456106859&ie=utf8&oe=gbk&cb=bd__cbs__l98142&format=json&tn=baidu'

        request = urllib2.Request(url)
        request.add_header("user-agent", "Mozilla/4.0")
        response = urllib2.urlopen(request, timeout=3)
        if response.getcode() != 200:
            return None
        return response.read().decode('gbk').encode('utf-8')