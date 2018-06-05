FROM ubuntu:bionic  
  
MAINTAINER Phocean <jc@phocean.net>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
VERSION=7.5.4 \  
GPG_KEY=2E1AC68ED40814E0 \  
LANGUAGE=fr \  
HOME=/home/anon  
  
WORKDIR $HOME  
  
RUN apt-get update &&\  
apt-get install -y --no-install-recommends \  
firefox libgtk2.0-0 xz-utils curl libcurl4 ca-certificates gnupg2 dirmngr &&\  
rm -rf /var/lib/apt/lists/*  
  
# Add TOR browser  
RUN curl -sSL -o tor.tar.xz
https://www.torproject.org/dist/torbrowser/${VERSION}/tor-browser-
linux64-${VERSION}_${LANGUAGE}.tar.xz &&\  
curl -sSL -o tor.tar.xz.asc
https://www.torproject.org/dist/torbrowser/${VERSION}/tor-browser-
linux64-${VERSION}_${LANGUAGE}.tar.xz.asc &&\  
gpg2 --batch --keyserver keys.gnupg.net --recv-keys ${GPG_KEY} &&\  
gpg2 --batch --verify tor.tar.xz.asc tor.tar.xz &&\  
tar xvf tor.tar.xz &&\  
rm -f tor.tar.xz* &&\  
mkdir Downloads &&\  
useradd -u 1000 anon &&\  
chown -R anon:anon $HOME  
  
VOLUME $HOME/Downloads  
  
USER anon  
  
CMD $HOME/tor-browser_fr/Browser/start-tor-browser  

