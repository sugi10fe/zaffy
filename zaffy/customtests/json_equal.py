# -*- coding: utf-8 -*-
import json
import util


def is_json_equal(left_value, right_value):
  left_str = util.unicode(left_value)
  right_str = util.unicode(right_value)

  if left_str == right_str:
    return True

  try:
    left_json = json.loads(left_str)
    right_json = json.loads(right_str)
    return left_json == right_json
  except ValueError:
    return False

