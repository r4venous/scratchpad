#!/usr/bin/env python3
# Quick base64 encode/decode utility
# Usage: python b64check.py encode "hello"
#        python b64check.py decode "aGVsbG8="

import base64
import sys

if len(sys.argv) != 3:
    print("Usage: b64check.py [encode|decode] <string>")
    sys.exit(1)

mode, data = sys.argv[1], sys.argv[2]

if mode == "encode":
    print(base64.b64encode(data.encode()).decode())
elif mode == "decode":
    try:
        print(base64.b64decode(data).decode())
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Unknown mode. Use encode or decode.")
