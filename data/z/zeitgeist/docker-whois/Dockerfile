# vim:set ft=dockerfile:  
# VERSION 1.0  
# AUTHOR: Alexander Turcic <alex@zeitgeist.se>  
# DESCRIPTION: whois (by Marco d'Itri) in a Docker container  
# TO_BUILD: docker build --rm -t zeitgeist/docker-whois .  
# SOURCE: https://github.com/alexzeitgeist/docker-whois  
# Pull base image.  
FROM debian:jessie  
MAINTAINER Alexander Turcic "alex@zeitgeist.se"  
# Compile whois  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
git \  
make \  
gcc \  
gettext \  
libidn11-dev && \  
git clone https://github.com/rfc1036/whois.git && \  
cd whois && \  
make && \  
make install && \  
cd .. && \  
rm -rf whois && \  
apt-get -y purge \  
git \  
make \  
gcc \  
gettext \  
libidn11-dev && \  
apt-get -y autoremove --purge && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
export uid=1000 gid=1000 && \  
groupadd --gid ${gid} user && \  
useradd --uid ${uid} \--gid ${gid} \--create-home user  
  
USER user  
WORKDIR /home/user  
  
ENTRYPOINT ["/usr/bin/whois"]  
CMD ["--help"]  

