"""The loadEnvironment function reads the contents of the
'environment.yml' if present. The return value is a list of strings
representing lines in the file."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from vistutils import getProjectRoot


def loadEnvironment(*args, **kwargs) -> list:
  """The loadEnvironment function reads the contents of the
  'environment.yml' if present. The return value is a list of strings
  representing lines in the file."""

  root = getProjectRoot()
  name = 'environment.yml'
  filePath = os.path.join(root, name)
