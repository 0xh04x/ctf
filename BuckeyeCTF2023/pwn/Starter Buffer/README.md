# BuckeyeCTF 2023 | pwn | Starter Buffer

by h04x

### Challenge Description 

![](./description.png)

#### Looking at the Source Code

Looking at the Source Code we can see that the script executes the print_flag() function if ```flag == 0x45454545```
There's also a input max set to 100 
My first idea is use a buffer overflow and overwrite the value of the flag variable.

When converting 0x45454545 to ASCII we get EEEE so we just have to spam E's lmao

Let's try that locally!

And we get a segmentation fault error! Great

[](./seg-fault-error.png)

#### Getting the flag

Let's try the same Exploit on the server-side

And we got the flag!

[](./flag.png)

`FLAG: bctf{wHy_WriTe_OveR_mY_V@lUeS}`