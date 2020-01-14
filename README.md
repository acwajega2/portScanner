# portScanner

# important notes
Before we get started with our sample program, let's see some of the socket
functions we are going to use.

sock = socket.socket (socket_family, socket_type)
Syntax for creating a socket

sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
Creates a stream socket

AF_INET
Socket Family (here Address Family version 4 or IPv4)

SOCK_STREAM
Socket type TCP connections

SOCK_DGRAM
Socket type UDP connections

gethostbyname("host")
Translate a host name to IPv4 address format

socket.gethostbyname_ex("host")
Translate a host name to IPv4 address format, extended interface

socket.getfqdn("8.8.8.8")
Get the fqdn (fully qualified domain name)

socket.gethostname()
Returns the hostname of the machine..

socket.error
Exception handling