"""ROBOT"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import QProcess, Signal, Slot


class Robot(QProcess):
  """ROBOT"""

  pub = Signal(str)

  @Slot(str)
  def receive(self, data: str) -> None:
    pass
