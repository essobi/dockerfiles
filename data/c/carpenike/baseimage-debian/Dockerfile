FROM debian:latest  
MAINTAINER carpenike <carpenike@gmail.com>  
  
# set version for s6 overlay  
ARG OVERLAY_VERSION="v1.18.1.5"  
ARG OVERLAY_ARCH="amd64"  
# set environment variables  
#ARG DEBIAN_FRONTEND="noninteractive"  
ENV HOME="/root" \  
TERM="xterm"  
ADD https://github.com/just-
containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz
/tmp  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
RUN \  
# update sources list  
apt-get clean && \  
apt-get update && \  
apt-get install -y \  
apt-utils \  
wget \  
curl && \  
  
# create abc user  
useradd -u 911 -U -d /config -s /bin/false abc && \  
usermod -G users abc && \  
  
# make our folders  
mkdir -p /app /config /defaults && \  
  
# cleanup  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*  
  
# add local files  
COPY root/ /  
  
ENTRYPOINT ["/init"]  

