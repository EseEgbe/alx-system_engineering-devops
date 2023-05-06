# Project Web Stack Debugging
Project done during **Software Engineering program** at **ALX**.
Its aim is to learn how to debug web stacks.

## Technologies
* Scripts are written in Bash 5.2.15
* Tested on Ubuntu 20.04 LTS

## Tasks To Complete

+ [x] 0. Strace is your friend<br/>_**[0-strace_is_your_friend.pp](0-strace_is_your_friend.pp)**_ contains a Puppet manifest that fixes a faulty server.
  + **Info**:
    + Using `strace`, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).
  + **HINT:**
    + `strace` can attach to a current running process.
    + You can use [tmux](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/) to run [strace](https://strace.io/) in one window and `curl` in another one.
