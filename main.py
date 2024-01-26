"""Main tester script."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations
import _pre
import os
import sys
import rospy
import std_msgs.msg as msg
from std_msgs.msg import Bool
from vistutils.dispatcher import Res


def func(self: Res) -> str:
  """Drop in replacement for __str__"""


def tester00() -> None:
  """Hello world"""
  stuff = ['hello world', os, sys, rospy, msg, _pre]
  for item in stuff:
    print(item)


def tester01() -> None:
  """ROS msg types"""
  for item in dir(msg):
    print(item)
  for item in dir(Bool):
    print(item)

  print(type(Bool.data))
  print(Bool.__slots__)

  print(sys.modules[Bool.__module__])

  print(sys.version)


def tester02() -> None:
  """lmao"""
  for (key, val) in rospy.__dict__.items():
    print(key, type(val))


def tester03() -> None:
  """yolo"""
  stuff = [k for (k, _) in sys.modules.items()]
  for item in stuff:
    print(item)


def tester04() -> None:
  """fuck"""
  res = Res('conda env export | grep -v "^prefix:" > environment.yml')
  print(res)


def tester05() -> None:
  """cunt"""
  res = Res('')


if __name__ == '__main__':
  tester04()
