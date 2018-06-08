FROM debian:stretch  
  
CMD ["/usr/bin/mpdscribble", "--host", "mpd", "--no-daemon", "--log", "-", "--
conf", "/etc/mpdscribble/mpdscribble.conf"]  
  
ADD 02apt-no-recom /etc/apt/apt.conf.d/  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
VOLUME /etc/mpdscribble  
  
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get -y install
mpdscribble  

