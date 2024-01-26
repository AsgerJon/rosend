"""The AdoptMeta provides a metaclass with the special property that
derived classes are not actually subclasses of baseclasses. Instead,
the metaclass copies from baseclasses into the derived class, subject to
conditions. The use case is for subclasses of the message types defined in
the std_msgs.msg module. The ros side retains the original class,
but creates a mimic for use by the main application class. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import sys
from typing import Tuple, Type

if sys.version_info.minor > 8:
  Bases = tuple[type]
else:
  Bases = Tuple[Type, Type]


class AdoptMeta(type):
  """AdoptMeta copies methods from base classes on to the derived class."""

  @staticmethod
  def _collectBase(bcls: type, ) -> dict:
    """Collects callables from given base class. """
    out = {}
    namespace = bcls.__dict__
    for (key, val) in namespace.items():
      if callable(val):
        if key in namespace:
          raise KeyError(key)
        out[key] = val
    return out

  @classmethod
  def __prepare__(mcls, name: str, bases: Bases, **kwargs) -> dict:
    """Prepares and returns the namespace object. """
