# Docker container for Syncthing  
#  
# docker build -t ptimof/syncthing .  
FROM debian:stretch  
  
MAINTAINER Peter Timofejew <peter@timofejew.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y wget  
  
# add syncthing user (Note: must match uid/gid on host computer)  
RUN groupadd -g 800 syncthing && \  
useradd -m -u 800 -g 800 syncthing  
  
# create binary directory that's r/w by syncthing  
RUN mkdir -p /srv && \  
chown syncthing:syncthing /srv  
  
# Version of Syncthing to retrieve  
# This is a crazy way of updating, but it is early in the dev cycle  
ENV VERSION 0.14.17  
# get binary from official distro  
WORKDIR /tmp  
RUN wget -q
https://github.com/syncthing/syncthing/releases/download/v${VERSION}/syncthing-
linux-amd64-v${VERSION}.tar.gz && \  
tar xf syncthing-linux-amd64-v${VERSION}.tar.gz && \  
cp syncthing-linux-amd64-v${VERSION}/syncthing /srv && \  
rm -r syncthing-linux-amd64-v${VERSION}.tar.gz syncthing-linux-
amd64-v${VERSION}  
  
# add in launch script  
ADD syncthingd /srv/syncthingd  
RUN chmod 755 /srv/syncthingd  
  
# change ownership to syncthing  
RUN chown syncthing:syncthing /srv/*  
  
#create sync dir and conf dir  
RUN mkdir /music /playlist /syncthing  
  
VOLUME /music  
VOLUME /playlist  
VOLUME /syncthing  
  
# run as syncthing  
USER syncthing  
  
EXPOSE 8000 22000 21025/udp  
  
CMD ["/srv/syncthingd", "--no-browser", "--no-restart", "--gui-address",
"https://0.0.0.0:8000" , "-home=/syncthing"]  

