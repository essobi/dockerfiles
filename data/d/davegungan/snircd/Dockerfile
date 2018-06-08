FROM ubuntu  
#FROM debian  
MAINTAINER Dave Gungan <gm@quakenet.org>  
  
RUN adduser -q snircd  
  
#general installs  
RUN apt-get update && apt-get install -y wget gcc make flex bison  
  
#tests  
#RUN apt-get install -y net-tools  
#RUN apt-get update && apt-get install -y irssi nano  
RUN echo "root:root" | chpasswd  
  
WORKDIR /home/snircd  
USER snircd  
  
RUN wget --default-page=snircd.tar.gz
https://api.github.com/repos/quakenet/snircd/tarball/ && tar -xf snircd.tar.gz
&& mv quakenet-snircd* snircd-src  
  
WORKDIR /home/snircd/snircd-src  
  
RUN ./configure -v --with-maxcon=10240 --enable-debug && make && make install  
  
WORKDIR /home/snircd/bin  
EXPOSE 6667  
EXPOSE 4400  
COPY ./ircd.conf /home/snircd/lib  
  
CMD ["./ircd", "-n", "-x", "999"]  

