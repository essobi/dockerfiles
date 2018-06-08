FROM ubuntu:xenial  
  
MAINTAINER Fernando Moro <fernando.moro@radmas.com>  
  
LABEL org.mejoratuciudad.vendor="Radmas Technologies"  
LABEL org.mejoratuciudad.image-name="mtc-plus-nginx"  
LABEL version="1.0"  
LABEL description="Web Server."  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#################################################  
# NGINX  
  
# Install PPA dependencies  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
software-properties-common  
  
# Add nginx PPA  
RUN \  
apt-add-repository -y ppa:nginx/stable  
  
# Update apt cache with PPA  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
nginx-full && \  
rm -rf /var/lib/apt/lists/*  
  
# Remove unused dependencies  
RUN \  
apt-get remove --purge -y \  
software-properties-common &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/var/cache/nginx"]  
  
#################################################  
# S6 OVERLAY  
  
USER root  
  
# install s6-overlay  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
ENTRYPOINT ["/init"]  

