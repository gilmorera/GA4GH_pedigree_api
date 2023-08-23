from .answer import answer

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown version"


__author__ = ["Bradley Lowekamp"]

__all__ = ["do_something", "answer"]
