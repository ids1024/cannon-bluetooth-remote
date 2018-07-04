#!/usr/bin/env python3

import sys
from subprocess import Popen, PIPE

DEVICE_NAME = "PY"

BUTTON_RELEASE = 0b10000000
BUTTON_FOCUS   = 0b01000000
BUTTON_TELE    = 0b00100000
BUTTON_WIDE    = 0b00010000
MODE_IMMEDIATE = 0b00001100
MODE_DELAY     = 0b00000100
MODE_MOVIE     = 0b00001000

device = sys.argv[1]
cmd = sys.argv[2] 

if cmd != 'pair':
    if cmd[0] == 'r':
        button = BUTTON_RELEASE
    elif cmd[0] == 'f':
        button = BUTTON_FOCUS
    elif cmd[0] == 't':
        button = BUTTON_TELE
    elif cmd[0] == 'w':
        button = BUTTON_WIDE
    else:
        print("No command")

    if cmd[1] == 'i':
        mode = MODE_IMMEDIATE
    elif cmd[1] == 'm':
        mode = MODE_MOVIE
    elif cmd[1] == 'd':
        mode = MODE_DELAY
    else:
        print("No Mode")

p = Popen(['btgatt-client', '-d', device],
          stdout=PIPE, stdin=PIPE, universal_newlines=True)

def wait_contain(s):
    while True:
        line = p.stdout.readline()
        if s in line:
            break

def write_value(*values):
    p.stdin.write("write-value " + ' '.join(map(str, values)) + '\n')
    p.stdin.flush()
    wait_contain("Write successful")

wait_contain("GATT discovery procedures complete")
write_value(0xf504, 3, *map(ord, DEVICE_NAME))
if cmd != 'pair':
    write_value(0xf506, button | mode)
