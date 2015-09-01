#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from tika_client import TikaClient


tikaclient = TikaClient('localhost', 9999)

#check if server is listening 
rtn = tikaclient.server_check()
if not rtn[0]:
    raise Exception("Server is not responding\nReason: " + rtn[1])

file_path = sys.argv[1]
rtn = tikaclient.extract_text(file_path)

if rtn[0]:
    print rtn[1]
else:
    "error " + rtn[1]
