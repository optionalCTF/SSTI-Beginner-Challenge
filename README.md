# Server Side Template Injection Challenge

## Difficulty: Easy

The goal of this challenge is to leak the secret key of the application. 
During presentation to the Ethical hacking society at Portsmouth University this was deployed onto TryHackMe.com and a flag.txt was placed within the working directory and one within the root directory.

## Privilege Escalation

The box employed a basic suid vulnerability with vim designed to introduce a beginner audience to GTFObins. (https://gtfobins.github.io/) so that in future challenges they have some basic resources to enumerate a system