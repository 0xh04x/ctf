# SunshineCTF 2023 | Web | BeepBoop Blog

by h04x

### Challenge Description 

![](./description.png)

#### Looking at the Website

The website is a blog for robots. 

![](./robots.png)

We can click on each post to view the full post
I captured the request to view each post in BurpSuite and then brute forced all of the blog posts from 0-1000

And post 608 is different because it has an attribut that the others don't have:
```hidden: true```

![](./flag.png)

`FLAG: sun{wh00ps_4ll_IDOR}`