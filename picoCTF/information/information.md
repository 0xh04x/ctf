# information
## Chall Auth: SUSIE

## Description

![](./description.png)

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](./cat.jpg)

## Solving

The first thing i will do is check the files information with exiftool

![](./exiftool.png)

The license string seems to be base64 encoded, so let's decode it!

![](./flag.png)

And there is the flag.


