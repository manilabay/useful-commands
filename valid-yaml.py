#!/usr/bin/env python

import yaml
import sys

if len(sys.argv) > 1:
  file = sys.argv[1]

with open(file, 'r') as stream:
    print(yaml.load(stream))
    #print(yaml.dump(stream))
