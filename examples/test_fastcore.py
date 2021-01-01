#!/usr/bin/env python

from fastcore.script import *

@call_parse
def main(msg:Param("The message", str),
         upper:Param("Convert to uppercase?", store_true)=False):
    "Print `msg`, optionally converting to uppercase"
    print(msg.upper() if upper else msg)

