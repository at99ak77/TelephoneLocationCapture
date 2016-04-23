# -*- coding:utf-8 -*-
from location_spider import code_manager
from location_spider import html_downloader
from location_spider import html_parser
from location_spider import sql_outputer
import time


class SpiderMain(object):
    def __init__(self):
        self.codes = code_manager.CodeManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = sql_outputer.SQLOutputer()

    def craw(self, root_head_code, start_index, end_index):

        self.codes.add_new_codes(root_head_code, start_index, end_index)
        while self.codes.has_new_code():
            time.sleep(0.1)
            new_code = self.codes.get_new_code()
            try:
                html_cont = self.downloader.download(new_code)
                if html_cont is None:
                    self.codes.add_new_code(new_code)
                    print 'craw %d fail' % new_code
                else:
                    result, code_data = self.parser.parse(new_code, html_cont)
                    if result:
                        self.outputer.collect_data(code_data)
                        print 'craw %d success' % new_code
                    else:
                        print 'craw %d blank' % new_code
            except:
                self.codes.add_new_code(new_code)
                print 'craw %d exception' % new_code

        self.outputer.close()


if __name__ == "__main__":
    root_head_codes = [173]

    for root_head_code in root_head_codes:
        obj_spider = SpiderMain()
        obj_spider.craw(root_head_code, 7000, 10000)
