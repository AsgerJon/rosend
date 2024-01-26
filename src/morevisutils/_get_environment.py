"""The getEnvironment function creates an 'environment.yml' file defining
the active environment."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from vistutils import getProjectRoot
from vistutils.dispatcher import Res


def getEnvironment(*args, **kwargs) -> str:
  """The getEnvironment function creates an 'environment.yml' file defining
  the active environment."""

  root = getProjectRoot()
  name = 'environment.yml'
  filePath = os.path.join(root, name)
  cmd = """conda env export | grep -v "^prefix:" > %s"""
  res = Res(cmd % filePath)
  if res:
    raise RuntimeError(res.err)

  return filePath
