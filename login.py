#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import requests
import urllib
import time


def login():
    """login work"""
    headers = {
        'Host': 'wuhan.pbb.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://wuhan.pbb.edu.cn/portal.php',
        # For security purposes, some fields (those with braces) are hidden. You can get them by yourself.
        'Cookie': 'PHPSESSID={phpsessid}; cernet_user_name={username}; cernet_password={password_encoded}',
        'Connection': 'keep-alive'
    }
    s = requests.Session()
    s.headers = headers
    post_data = {
        # For security purposes, some fields (those with braces) are hidden. You can get them by yourself.
        'client_ip': '{client_ip}',
        'bras_ip': '{bras_ip}',
        'domain_id': '1',
        'op_type': 'portal',
        'refer': 'http://wuhan.pbb.edu.cn/portal.php',
        'user_name': '{username}',
        'password': '{password}',
    }
    r = s.post('http://wuhan.pbb.edu.cn/php/p_login_net.php', data=post_data, verify=False)
    return r.status_code


if __name__ == '__main__':
    logging.basicConfig(
        level    = logging.DEBUG,
        format   = '%(asctime)s [%(levelname)s] %(message)s',
        datefmt  = '%a, %Y-%m-%d, %H:%M:%S',
        filename = 'login_cernet.log',
    )
    # logger = logging.getLogger(__name__)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    while 1:
        logging.info('Start logging in')
        # read database here
        success = '<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML>'
        if urllib.urlopen('http://captive.apple.com').read() == success:
            logging.info('You have already logged in')
        else:
            status = login()
            if status == 200:
                logging.info('Login successful, status code = {0}'.format(status))
            else:
                logging.warn('Login failed, status code = {0}'.format(status))
        time.sleep(300)
