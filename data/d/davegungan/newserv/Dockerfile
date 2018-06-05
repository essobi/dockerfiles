FROM ubuntu  
  
MAINTAINER Dave Gungan <gm at quakenet.org>  
  
RUN adduser -q newserv  
  
#general installs  
RUN apt-get update && apt-get install -y wget gcc make  
  
#installs for newserv  
RUN apt-get update && apt-get install -y python flex bison libpcre3-dev
liblua5.1-0 liblua5.1-0-dev  
  
#tests  
#RUN apt-get install -y net-tools  
#RUN apt-get update && apt-get install -y irssi nano  
#RUN echo "root:root" | chpasswd  
WORKDIR /home/newserv  
USER newserv  
  
RUN wget --default-page=newserv.tar.gz
https://api.github.com/repos/quakenet/newserv/tarball/ && tar -xf
newserv.tar.gz && mv quakenet-newserv* newserv  
  
WORKDIR /home/newserv/newserv  
  
RUN ./configure -v && make && make install  
  
COPY newserv.conf .  
  
CMD ["./newserv"]  
  

