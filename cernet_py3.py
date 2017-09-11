#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re


class Cernet(object):
    def __init__(self, username, password):
        self.params = {}
        self.params['user_name'] = username
        self.params['password'] = password

    def __get_login_data(self):
        req = urllib.request.Request('http://wuhan.pbb.edu.cn/portal.php')
        req.add_header('Host', 'wuhan.pbb.edu.cn')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0')
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
        req.add_header('Accept-Encoding', 'gzip, deflate')
        req.add_header('Connection', 'keep-alive')
        req.add_header('Upgrade-Insecure-Requests', '1')
        req.add_header('Cache-Control', 'max-age=0')
        r = urllib.request.urlopen(req)
        html = r.read().decode('cp936')
        param_key = ['client_ip', 'bras_ip', 'domain_id', 'op_type', 'refer']
        for key in param_key:
            self.params[key] = re.findall('<input type="hidden" name="{}" value="(.*?)" />'.format(key), html)[0]
        print(self.params)

    def __post_login(self):
        req = urllib.request.Request('http://wuhan.pbb.edu.cn/php/p_login_net.php')
        data = urllib.parse.urlencode(self.params).encode('utf-8')
        req.add_header('Host', 'wuhan.pbb.edu.cn')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0')
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
        req.add_header('Accept-Encoding', 'gzip, deflate')
        req.add_header('Referer', 'http://wuhan.pbb.edu.cn/portal.php')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        req.add_header('Content-Length', str(len(data)))
        req.add_header('Connection', 'keep-alive')
        req.add_header('Upgrade-Insecure-Requests', '1')
        f = urllib.request.urlopen(req, data)
        print(f.read().decode('cp936'))

    def login(self):
        self.__get_login_data()
        self.__post_login()


if __name__ == '__main__':
    cernet = Cernet(input('Username: '), input('Password: '))
    cernet.login()

