# -*- coding:utf-8 -*-
import json


class HtmlParser(object):

    def parse(self, code, html_cont):

        json_data = html_cont[20: len(html_cont) - 2]
        data = json.loads(json_data)
        res_dict = {}
        if len(data['data']) == 0:
            result = False
        else:
            result = True
            res_dict['code'] = code
            res_dict['loc'] = data['data'][0]['prov'] + data['data'][0]['city']
            res_dict['type'] = data['data'][0]['type']
        return result, res_dict

