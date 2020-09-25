### [shebang (#!)](https://en.wikipedia.org/wiki/Shebang_(Unix))
`#!/bin/sh` – Execute the file using the Bourne shell, or a compatible shell, assumed to be in the /bin directory
`#!/bin/bash` – Execute the file using the Bash shell
`#!/usr/bin/env python3` – Execute with a Python interpreter, using the program search path to find it
`#!/bin/false` – Do nothing, but return a non-zero exit status, indicating failure. Used to prevent stand-alone execution of a script file intended for execution in a specific context, such as by the . command from sh/bash, source from csh/tcsh, or as a .profile, .cshrc, or .login file.

### [missing-semester](https://missing.csail.mit.edu/2020/course-shell/)

>Try to execute the file, i.e. type the path to the script (`./semester`) into your shell and press enter. Understand why it doesn’t work by consulting the output of `ls` (hint: look at the **permission bits** of the file).
>Run the command by explicitly starting the sh interpreter, and giving it the file semester as the first argument, i.e. `sh semester`. Why does this work, while `./semester` didn’t?
>Look up the `chmod` program (e.g. use `man chmod`).
>Use `chmod` to make it possible to run the command `./semester` rather than having to type `sh semester`. How does your shell know that the file is supposed to be interpreted using `sh`? See this page on the **shebang** line for more information.
