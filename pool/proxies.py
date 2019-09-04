# !/usr/bin/python
# -*- coding:utf-8 -*-
# __Author__: v

import requests, csv, time
import random
from bs4 import BeautifulSoup
from pool import header


def get_proxies():
    proxies_list = []
    for n in range(1, 10):
        print('正在搜集第{}页信息...'.format(n))
        url = 'https://www.kuaidaili.com/free/inha/{}/'.format(n)
        r = requests.get(url, headers = header.randUserAgent())
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'lxml')
            proxies = soup.find_all('tr')[1:]
            for info in proxies:
                # print(info)
                ip = info.find(attrs={"data-title": "IP"}).text
                print(ip)
                port = info.find(attrs={"data-title": "PORT"}).text
                proxy = [ip + ':' + port]
                proxies_list.append(proxy)
                print(proxies_list)
            time.sleep(2)
            save_proxies(proxies_list)
    # return proxies_list

def save_proxies(text):

    with open('/Users/a1/Desktop/python3_tools/pool/proxy.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in text:
            # print(row)
            writer.writerow(row)
    print('保存成功')

def randProxy():
    with open('/Users/a1/Desktop/python3_tools/pool/proxy.csv', 'r') as f:
        proxies = f.read().split('\n')[: -1]
        # print(random.choice(proxies))
        proxy = {
            'HTTP': random.choice(proxies),
            'HTTPS': random.choice(proxies)
        }
        return proxy
        # r = requests.get('http://www.ip138.com/', headers = header.randUserAgent(), proxies=proxy, timeout=5, verify=False)
        # print(r)
        # if r.status_code == 200:
        #     return proxy
        # else:
        #     time.sleep(3)
        #     randProxy()


# def verify():
#     with open('/Users/a1/Desktop/python3_tools/pool/proxy.csv', 'r') as f:
#         proxies = f.read().split('\n')[: -1]
#     r = requests.get('http://www.ip138.com/', headers = header.randUserAgent(), timeout=7)
#     if r.status_code != 200:



if __name__ == '__main__':
    # 第一次执行要通过get_proxies()获取ip
    # get_proxies()
    print(randProxy())
