# -*- coding: utf-8 -*-

from wox import Wox
import webbrowser
import query

class Main(Wox):

    def query(self, q):
        result = query.do(q)
        item = {
            'Title': result['title'],
            'IcoPath': 'icon.png',
        }
        if result['valid']:
            item['JsonRPCAction'] = {
                'method': 'openUrl',
                'parameters': [result['url']],
            }
        return [item]

    def openUrl(self, url):
        webbrowser.open(url)

if __name__ == '__main__':
    Main()
