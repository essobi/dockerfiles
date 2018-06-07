FROM debian:jessie  
MAINTAINER GP Orcullo <kinsamanka@gmail.com>  
  
ENV TERM dumb  
ENV ROOTFS /opt/rootfs  
  
# apt config: silence warnings and set defaults  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
ENV LC_ALL C  
ENV LANGUAGE C  
ENV LANG C  
  
# container OS  
RUN echo 'APT::Install-Recommends "0";\nAPT::Install-Suggests "0";' > \  
/etc/apt/apt.conf.d/01norecommend  
  
# install required dependencies  
RUN apt-get update && \  
apt-get -y install \  
multistrap \  
proot  
  
ADD test.conf /  
RUN multistrap -f /test.conf -a amd64 -d /rootfs  
RUN proot -r /rootfs /var/lib/dpkg/info/dash.preinst install  
RUN proot -r /rootfs dpkg --configure -a  

