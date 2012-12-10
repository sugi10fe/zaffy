# -*- coding: utf-8 -*-
from lxml import etree

def do_xpathlist(value, xpath, namespaces=None):
  """ 常に list 形式で返す """
  root = etree.fromstring(str(value))
  result = root.xpath(xpath, namespaces=namespaces)
  return result

def do_xpath(value, xpath, namespaces=None):
  """ 返り値が1件だけの場合は中身を取り出して返す """
  root = etree.fromstring(str(value))
  result = root.xpath(xpath, namespaces=namespaces)
  if len(result) == 1:
    return result[0]
  return result

do_tocmp_on_asserting = [
  ['xpathlist', 2],
  ['xpath', 2]
]
