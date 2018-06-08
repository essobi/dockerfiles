FROM debian:stretch  
  
CMD ["/usr/bin/ncmpcpp", "--host", "mpd"]  
  
ADD 02apt-no-recom /etc/apt/apt.conf.d/  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get -y install ncmpcpp  

