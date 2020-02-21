# coding: utf-8
'''
eabanner : e-Attestations banner module

A simple utility module for banner display.

- colored : for a colored banner
- banner : for the non colored version

Enjoy !

e-Attestations
'''

from .banner import banner
from .colored import colored

__all__ = ['colored', 'banner']
__version__ = '0.1'