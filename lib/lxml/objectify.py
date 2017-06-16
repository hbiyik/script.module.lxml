import abi
import sys


__m = abi.load("script.module.lxml", "objectify")
import sys
sys.modules[__name__] = __m
