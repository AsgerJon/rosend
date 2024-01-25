"""The AdoptMeta provides a metaclass with the special property that
derived classes are not actually subclasses of baseclasses. Instead,
the metaclass copies from baseclasses into the derived class, subject to
conditions. The use case is for subclasses of the message types defined in
the std_msgs.msg module. The ros side retains the original class,
but creates a mimic for use by the main application class. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations
