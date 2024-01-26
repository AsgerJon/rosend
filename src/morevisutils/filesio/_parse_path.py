"""The parsePath function provides common parsing for file paths."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
from typing import Optional, Any

from vistutils import stringList, searchKey, getProjectRoot, maybeType
from vistutils.waitaminute import typeMsg


def _validateString(value: Any) -> Any:
  """Validates that the value received as a string."""
  if isinstance(value, bytes):
    return value.decode('utf8')
  if isinstance(value, str):
    return value
  if value is not None:
    expType = str
    msg = typeMsg('fileName', value, expType)
    raise TypeError(msg)


def _parseFileName(**kwargs) -> Optional[str]:
  """Parses keyword arguments for file name"""
  nameKeys = stringList("""fileName, fid, file""")
  nameKwarg = searchKey(*nameKeys, **kwargs)
  name = _validateString(nameKwarg)
  baseName, dirName = os.path.basename(name), os.path.dirname(name)
  if os.path.isabs(name):
    return baseName
  return name


def _parseDirName(**kwargs) -> Optional[str]:
  """Parses keyword arguments for directory name"""
  dirKeys = stringList("""dir, dirName, directory, folder""")
  dirKwarg = searchKey(*dirKeys, **kwargs)
  name = _validateString(dirKwarg)
  baseName, dirName = os.path.basename(name), os.path.dirname(name)
  if os.path.isabs(name):
    return dirName
  return name


def validatePathLike(maybePath: str) -> str:
  """Validates that the given path might describe a path."""
  if maybePath is None:
    raise UnboundLocalError('Is none')
  if not isinstance(maybePath, str):
    e = """Expected path to be 'str' but received: '%s' of type '%s'!"""
    raise TypeError(e % (maybePath, type(maybePath)))
  failChars = """ \\ : * ? " < > | """.replace(' ', '')
  badChars = [c for c in failChars if c in maybePath]
  if badChars:
    e = """Given path: %s contains illegal characters: '%s'!"""
    raise ValueError(e % (maybePath, ' '.join(badChars)))
  if maybePath not in ['.', '/'] and len(maybePath) < 2:
    raise ValueError('Path too short!')
  if os.path.isabs(maybePath):
    return maybePath
  if maybePath[:2] == './':
    return maybePath
  return './%s' % maybePath


def _parsePathKwarg(**kwargs) -> Optional[str]:
  """Parses keyword arguments for full path"""
  pathKeys = stringList("""path, fullPath, fid""")
  pathKwarg = searchKey(*pathKeys, **kwargs)
  fullPath = _validateString(pathKwarg)
  try:
    return validatePathLike(fullPath)
  except UnboundLocalError as e:
    if 'is none' not in str(e).lower():
      raise e
  dirName, fileName = _parseDirName(**kwargs), _parseFileName(**kwargs)
  try:
    dirName = _parseDirName(**kwargs)
  except UnboundLocalError as e:
    if 'is none' not in str(e).lower():
      raise e
  try:
    fileName = _parseFileName(**kwargs)
  except UnboundLocalError as e:
    if 'is none' not in str(e).lower():
      raise e
  if dirName is not None:
    if fileName is not None:
      return os.path.join(dirName, fileName)


def parsePath(*args, **kwargs) -> str:
  """Checks file Path"""

  pathKeys = stringList("""path, fullPath, fid""")
  pathKwarg = searchKey(*pathKeys, **kwargs)
  try:
    return _validateString(pathKwarg)
  except UnboundLocalError as e:
    if 'is none' not in str(e):
      raise e
  strArgs = maybeType(str, *args)
  if strArgs:
    if all([isinstance(arg, str) for arg in args]):
      return str(os.path.join(*strArgs))
  raise ValueError('unable to parse!')
