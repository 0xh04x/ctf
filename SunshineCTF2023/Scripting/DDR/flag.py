from pwn import *

p = remote('chal.2023.sunshinectf.games', 23200)

p.recvuntil(b'-- Press ENTER To Start --')
p.sendline()
p.recvline()
p.recvline()

for i in range(255):
        a = p.recvline()
        a = a[:-2].decode()
        print(a)
        sol = ""
        for c in a:
                if c == "⇦":
                        sol += 'a'
                elif (c == "⇧"):
                        sol += 'w'
                elif (c == "⇨"):
                        sol += 'd'
                elif (c == "⇩"):
                        sol += 's'
       
        p.sendline(sol.encode())

print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())

