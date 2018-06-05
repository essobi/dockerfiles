# Dockerfile to build Swiss flavor of minimal Debian Wheezy  
FROM debian:wheezy  
MAINTAINER rezzonic  
  
EXPOSE 23  
RUN echo "deb http://mirror.switch.ch/ftp/mirror/debian/ wheezy main contrib
non-free" > /etc/apt/sources.list  
RUN echo "deb http://mirror.switch.ch/ftp/mirror/debian/ wheezy-updates main
contrib non-free" >> /etc/apt/sources.list  
RUN echo "deb http://security.debian.org wheezy/updates main contrib non-free"
>> /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y dist-upgrade  
RUN apt-get -y install python  
RUN apt-get clean  
COPY ascii-telnet-server-scitas.py /root/ascii-telnet-server-scitas.py  
COPY ascii-telnet-server.py /root/ascii-telnet-server.py  
COPY LICENSE /root/LICENSE  
ADD http://scitas-data.epfl.ch/presentations/scitas-telnet.txt /root/  
RUN echo "#!/bin/sh" >> /root/runme.sh  
RUN echo "python /root/ascii-telnet-server-scitas.py -f /root/scitas-
telnet.txt" >> /root/runme.sh  
RUN echo "sleep 10000" >> /root/runme.sh  
CMD "sh" "/root/runme.sh"  
  

