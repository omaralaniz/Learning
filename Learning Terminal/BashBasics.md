### Terminal Unix Shell For Basics

_What is Terminal Unix?_

> ... is a command-line interpreter and shell, and the shell gives you a command line to interact with the UNIX systems. Allow the users to interact with the system files that uses command language and scripting language. (Users usually use terminal a.k.a shell emulator to interact with the system). The user may use an ssh (secure shell) for server side needs

Terminal Commands:

| Command  | Description                                                  |
| :------- | ------------------------------------------------------------ |
| ssh      | is a cryptographic network protocol allows you to connect to system remotely and securely, in otherwise, unsecure shell. Allows command line login<br />Example:<br />`ssh bandit0@bandit.labs.overthewire.org -p 2220` -p is the port flag<br />`-t disables pseudo-terminal` |
| du       | disk usage. Displays the file space disk usage<br />`du -a` -a shows in a human readable way to display disk usage |
| find     | Searches for file in any directory you specify.<br />Example:<br />`find X -name "Y"` <br />`find X -name "*.jpg"` search for any file that is a .jpg<br />`find X -type f ` "-type f" looks for only files<br />`find X -type f -size n[cwbkMG]` "-size" size of file and "n" size you are<br />looking for. 'c' bytes 'w' two bytes 'k' kilobytes 'M' megabytes and 'G' Gigabytes |
| file     | `file <filename>` echoes the type of the file and description |
| grep     | `grep <variable>` anything related to the variable?          |
| strings  |                                                              |
| tar      |                                                              |
| gzip     |                                                              |
| bzip2    |                                                              |
| telnet   | `telnet localhost 30000` connects to the host `localhost` on port `30000` <br />connects to another host using the TELNET protocol |
| nc       |                                                              |
| openssl  | program allows crypto functions with a variety of OpenSSL crypto library |
| s_client | command under `openssl` e.g `openssl s_client -connect host:port` |
| nmap     |                                                              |

Great Things to Know:

> * To add a space to a filename in terminal `\<space> `

Funny things:

> * ​	If a filename is "-" and when you try to use `cat -` command it will think "- " is the Unix STDIN. So, to `cat -`  you do this instead `cat ./-` forcing the "cat" to see it as a file!

Overthewire.org Bandit:

> Bandit 6:
>
> DXjZPULLxYr17uwoI01bNLQbtFemEgo7
>
> Bandit 7:
>
> HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
>
> Bandit 8:
>
> cvX2JJa4CFALtqS87jk27qwqGhBM9plV
>
> Bandit 9:
>
> UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
>
> Bandit 10:
>
> truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
>
> Bandit 11:
>
> IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
>
> Bandit 12:
>
> 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
>
> Bandit 13:
>
> 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
>
> Bandit 14:
>
> 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
>
> Bandit 15:
>
> BfMYroe26WYalil77FoDi9qh59eK5xNr
>
> Bandit 16:
>
> cluFn7wTiGryunymYOu4RcffSxQluehd
>
> Bandit 17:
>
> Go to $HOME and there you will find a key
>
> Bandit 18:
>
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
>
> Bandit 19:
>
> IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
>
> Bandit 20:
>
> 

 