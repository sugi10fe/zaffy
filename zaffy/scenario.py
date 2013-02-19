# -*- coding: utf-8 -*-
from assertionfailed import AssertionFailed
from baseaction import ActionException


class Scenario(object):
  def __init__(self, setting, doc, actions, parent=None):
    self.setting = setting
    self.doc = doc
    self.parent = parent
    self.localvar = {}

    self._action_queue = actions
    self._finished_actions = []

  def __getattr__(self, item):
    return getattr(self.setting, item)

  @property
  def actions(self):
    return self._finished_actions

  def run(self, global_env):
    # 一時対応
    if not self.parent:
      type.__getattribute__(global_env["const"], 'init_scenario')()
      type.__getattribute__(global_env["preset"], 'init_scenario')()
    # ここまで

    global_env["scenario"] = self
    global_env["local"] = self.localvar

    while self._action_queue:
      self._run_action(global_env)

    if self.parent:
      global_env["scenario"] = self.parent
      global_env["local"] = self.parent.localvar

  def add_action(self, action):
    self._action_queue.append(action)

  def _run_action(self, global_env):
    action = self._action_queue.pop(0)
    finished_actions = self._finished_actions

    global_env["actions"] = finished_actions
    global_env["action_index"] = len(finished_actions)
    global_env["this"] = action
    global_env["last"] = finished_actions[-1] if finished_actions else None
    try:
      action.run_action(global_env)
      action.run_assert(global_env)
    except (ActionException, AssertionFailed) as e:
      e.action_index = len(finished_actions)
      raise e
    finally:
      finished_actions.append(action)

