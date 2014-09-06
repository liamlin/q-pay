"""
Settings used by q_pay project.

This consists of the general produciton settings, with an optional import of any local
settings.
"""

# Import production settings.
from q_pay.settings.production import *

# Import optional local settings.
try:
    from q_pay.settings.local import *
except ImportError:
    pass