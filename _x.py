from pwn import *
import sys

# CONTEXT, BABY.
context.terminal = ['urxvt', '-e', 'sh', '-c']
context.log_level = "DEBUG"
context.arch = "i386"
#context.arch = "amd64"

HOST = None
PORT = None

THE_THING = None
#THE_THING = "./binary lol1 lol2"
#THE_THING = "strace ./binary lol1 lol2"

REMOTE = 'remote' in sys.argv
DEBUG = 'debug' in sys.argv

def make_remote():
    if REMOTE:
        r = remote(HOST, PORT)
    elif DEBUG:
        r = debug(THE_THING.split(" "), get_breakpoints())
        #r = gdb.debug(BINARY_NAME, get_breakpoints() + custom_gdbscript)
    else:
        r = process(THE_THING.split(" "))
    return r

# DEBUGGING STUFF

# With <3 for you and for
# binaries that don't setvbuf their shit.
custom_gdbscript = '''
continue
call setvbuf(stdout, 0, 2, 0)
continue
'''

def get_pie_breakpoints():
    return '\n'.join(["pie breakpoint * " + hex(x) for x in BPS.values()])

def get_breakpoints():
    return '\n'.join(["b * " + hex(x) for x in BPS.values()])

# INTERACTION STUFF
MENU_DELIM = '>'

def menu():
    return rtil(MENU_DELIM)

# BREAKPOINTS LIST
BPS = {}
#BPS["main"] = 0xdeadbeef

r = make_remote()

# SHORTCUTS
rtil = r.readuntil
readl = r.readline
send = r.send
sendl = r.sendline
senda = r.sendafter
sendla = r.sendlineafter

# FUN

# gdb.attach(r, get_breakpoints())

r.interactive()

