# build twister from source  
# see accompanying README.md  
# and upstream source instructions http://twister.net.co/  
FROM ubuntu:precise  
MAINTAINER Lex Lapax <lexlapax@gmail.com>  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
# run all build / compile steps from one step, reducing the committed image
size  
# too many intermediate packages that are not needed in the final image  
ADD https://raw.github.com/lexlapax/dockerfile-twisterd/master/build.sh
/root/build.sh  
  
RUN chmod +x /root/build.sh  
WORKDIR /root  
RUN ./build.sh  
  
EXPOSE 4433 4434 28332 28333 29333 29333/udp  
  
CMD ["/bin/bash", "-i"]  
CMD ["/usr/local/bin/twisterd"]  

