# Nice netcat...
## Chall Auth: SYREAL

## Description



There is a nice program that you can talk to by using this command in a shell: nc mercury.picoctf.net 7449, but it doesn't speak English...

## Solving

When connecting to ```nc mercury.picoctf.net 7449``` i got this output:

```112 105 99 111 67 84 70 123 103 48 48 100 95 107 49 116 116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 55 99 48 56 50 49 102 53 125 10```

For me this looks like numbers that are ASCII values

I just used an online decimal to ASCII converter and got the flag

## FLag

```picoCTF{g00d_k1tty!_n1c3_k1tty!_7c0821f5}```