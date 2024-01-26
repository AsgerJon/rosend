"""The savesLine function receives any number of positional arguments and
prints their string representations to the disk. The first positional
argument is expected to be the file path, unless the file path is provided
in the keyword arguments. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from morevisutils.filesio import parsePath


def saveLines(*args, **kwargs) -> str:
  """The savesLine function receives any number of positional arguments and
  prints their string representations to the disk. The first positional
  argument is expected to be the file path, unless the file path is provided
  in the keyword arguments. """

  filePath = parsePath(**kwargs)
  lines = [arg if isinstance(arg, str) else str(arg) for arg in args]
  data = '\n'.join(lines)
  with open(filePath, 'w') as f:
    f.write(data)

  return filePath
