FROM ubuntu:14.04  
MAINTAINER Eric Schultz <eric@startuperic.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen en_US en_US.UTF-8  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty multiverse" >>
/etc/apt/sources.list  
  
RUN apt-get update -q  
RUN apt-get install -qy --force-yes sabnzbdplus sabnzbdplus-theme-classic
sabnzbdplus-theme-mobile sabnzbdplus-theme-plush par2 python-yenc unrar unzip  
  
VOLUME /config  
VOLUME /data  
  
EXPOSE 8080 9090  
ENTRYPOINT ["/usr/bin/sabnzbdplus"]  
CMD ["--config-file", "/config", "--server", ":8080"]  

