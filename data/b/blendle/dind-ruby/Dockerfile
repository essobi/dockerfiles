FROM blendle/ruby:2.2  
MAINTAINER Jean Mertz <jean@blendle.com>  
  
ENTRYPOINT ["wrapdocker"]  
  
ENV LOG=file  
VOLUME /var/lib/docker  
  
RUN apk-install iptables ca-certificates lxc e2fsprogs wget docker socat perl
\  
device-mapper coreutils  
  
RUN wget -qO- https://get.docker.com/builds/Linux/x86_64/docker-1.6.2 >
/usr/bin/docker  
RUN wget -qO-
https://raw.githubusercontent.com/jpetazzo/dind/master/wrapdocker >
/usr/local/bin/wrapdocker  
RUN chmod +x /usr/bin/docker /usr/local/bin/wrapdocker  

