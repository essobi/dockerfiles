FROM ubuntu:xenial  
  
MAINTAINER Fernando Moro <fernando.moro@radmas.com>  
  
LABEL org.mejoratuciudad.vendor="Radmas Technologies"  
LABEL org.mejoratuciudad.image-name="mtc-plus-rsyslog"  
LABEL version="1.0"  
LABEL description="Centralized log server."  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#################################################  
# RSYSLOG  
  
# Install PPA dependencies  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
software-properties-common  
  
# rsyslog PPA  
RUN \  
add-apt-repository ppa:adiscon/v8-stable  
  
# Install rsyslog  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
rsyslog && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# S6 OVERLAY  
  
USER root  
  
# install s6-overlay  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
ENTRYPOINT ["/init"]  

