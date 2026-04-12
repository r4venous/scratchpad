#!/usr/bin/env python3
# Minimal hexdump
import sys

def hexdump(data: bytes, width: int = 16):
    for i in range(0, len(data), width):
        chunk = data[i:i+width]
        hex_part = " ".join(f"{b:02x}" for b in chunk)
        asc_part = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        print(f"{i:08x}  {hex_part:<{width*3}}  |{asc_part}|")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else None
    data = open(path, "rb").read() if path else sys.stdin.buffer.read()
    hexdump(data)
