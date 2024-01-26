"""Place at start"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import sys
from vistutils import applyEnv, getProjectRoot
from vistutils.dispatcher import Res

try:
  applyEnv(verbose=False)
  initialized = True
except Exception as exception:
  print('Failed to apply .env!')
  print('Exception type: ' % exception.__class__.__qualname__)
  print('Received: %s' % str(exception))

cmd = 'conda --version'

# if res.err:
#   print(res)
#
# root = getProjectRoot()
# print(root)
sys.modules['__main__'].__file__

#  vistutils.dispatcher.Res: Fixed __str__
