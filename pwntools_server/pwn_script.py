from pwn import *

target = remote("127.0.0.1", 65432)
target.sendline("flag{we_beleaf_in_your_re_future}")
# target.
target.interactive()
