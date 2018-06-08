FROM ubuntu:yakkety  
  
MAINTAINER Cougar <cougar@random.ee>  
  
ENV TINI_VERSION v0.13.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install wget python imagemagick libboost-iostreams1.60.0 libboost-
system1.60.0 libboost-filesystem1.60.0 libboost-program-options1.60.0  
  
RUN wget
https://mapcrafter.org/packages/ubuntu/yakkety/main/mapcrafter_2.3.1-1_amd64.deb  
RUN dpkg -i mapcrafter_2.3.1-1_amd64.deb  
  
RUN apt-get -y purge wget python imagemagick && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/minecraft-server", "/www"]  
  
ADD render.conf ./  
CMD ["mapcrafter", "-c", "./render.conf", "-j", "2"]  

