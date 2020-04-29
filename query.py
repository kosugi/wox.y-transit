# -*- coding: utf-8 -*-
#
# launch “Y!J Transit” with two station names (from, to).
#

import re
from urllib.request import quote

def u(value):
    return quote(value.encode('UTF-8'))

def parse_names(q):
    m = re.match(r'''\A\s*(\S+?)(?:\s+|(?:\s*[\u002d\u007e\u00ad\u058a\u05be\u1400\u1806\u2010\u2011\u2012\u2013\u2014\u2015\u2053\u207b\u208b\u2212\u2e3a\u2e3b\u301c\uff5e\u30a0\ufe58\ufe63\uff0d]\s*))(\S+)\s*\Z''', q.replace(u'　', u' '))
    if m:
        return m.groups()

def build_url(src, dest):
    return u'''http://transit.yahoo.co.jp/search/result?from={src}&to={dest}'''.format(src=u(src), dest=u(dest))

def make_item(valid, url, title):
    return {
        'valid': valid,
        'url': url,
        'title': title,
    }

def do(q):
    names = parse_names(q)
    if names:
        src, dest = names
        url = build_url(src, dest)
        return make_item(True, url, 'Query routes from {src} to {dest}'.format(src=src, dest=dest))
    else:
        return make_item(False, '', 'type “from” and “to” station names')
