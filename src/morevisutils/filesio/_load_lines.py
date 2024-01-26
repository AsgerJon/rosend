"""The loadLines function receives a path to a file and returns the text
lines contained in it."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from morevisutils.filesio import parsePath


def loadLines(*args, **kwargs) -> list:
  """The loadLines function receives a path to a file and returns the text
  lines contained in it."""

  filePath = parsePath(*args, **kwargs)
  data = None
  with open(filePath, 'r', encoding='utf-8') as f:
    data = f.readlines()
  if data is not None:
    return data
