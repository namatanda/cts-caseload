"""
Top level API (:mod:`cts_caseload`)
======================================================
"""

from .core import example_function

try:
    from ._version import __version__
except Exception:
    __version__ = "999"

__author__ = """Stan. M"""
__email__ = "mwagichimu@gmail.com"


__all__ = [
    "example_function",
    "__version__",
]
