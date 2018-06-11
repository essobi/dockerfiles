FROM ubuntu:17.04  
MAINTAINER Nick McFaul <n@mcf.io>  
  
# set version for s6 overlay  
ARG S6_OVERLAY_VERSION="v1.19.1.1"  
# set environment variables  
ARG DEBIAN_FRONTEND="noninteractive"  
ENV TERM="xterm" LANGUAGE="en_US.UTF-8" LANG="en_US.UTF-8" LC_ALL="C.UTF-8"  
# update distribution install apt-utils and locales  
RUN apt-get update && \  
apt-get install -y \  
apt-utils \  
dirmngr \  
locales \  
curl \  
tzdata \  
&& \  
# Fetch and extract S6 overlay  
curl -J -L -o /tmp/s6-overlay-amd64.tar.gz https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz && \  
tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \  
# Add user  
useradd -U -d /config -s /bin/false mcf && \  
usermod -G users mcf && \  
# Setup directories  
mkdir -p \  
/app \  
/config \  
/defaults \  
&& \  
# Cleanup  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
# Add local files  
COPY root/ /  
  
ENTRYPOINT ["/init"]

