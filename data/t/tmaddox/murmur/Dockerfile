# Mumble VoIP Server  
#  
# VERSION: 1.0  
FROM ubuntu:14.04  
MAINTAINER Thomas Maddox <thomas.e.maddox@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y mumble-server  
  
VOLUME /var/lib/mumble-server  
WORKDIR /var/lib/mumble-server  
  
USER mumble-server  
ENTRYPOINT ["/usr/sbin/murmurd", "-ini", "/var/lib/mumble-server/mumble-
server.ini"]  
CMD ["-fg", "-v"]  

