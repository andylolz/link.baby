import sys


if len(sys.argv) > 1 and 'behave' in sys.argv[1]:
    from .testing import *
else:
    try:
        from .local import *
    except ImportError:
        from .base import *
