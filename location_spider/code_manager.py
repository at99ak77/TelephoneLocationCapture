# -*- coding:utf-8 -*-


class CodeManager(object):

    def __init__(self):
        self.codes = []

    def add_new_code(self, code):
        self.codes.append(code)

    def add_new_codes(self, head_code, start_index, end_index):
        index_code = head_code * 10000 + start_index
        border = head_code * 10000 + end_index
        while index_code < border:
            self.add_new_code(index_code)
            index_code += 1

    def has_new_code(self):
        return len(self.codes) != 0

    def get_new_code(self):
        new_code = self.codes.pop(0)
        return new_code
