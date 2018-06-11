# vim:set ft=dockerfile:  
# VERSION 1.0  
# AUTHOR: Alexander Turcic <alex@zeitgeist.se>  
# DESCRIPTION: testssl in a Docker container  
# TO_BUILD: docker build --rm -t zeitgeist/docker-testssl .  
# SOURCE: https://github.com/alexzeitgeist/docker-testssl  
# Pull base image.  
FROM debian:jessie  
MAINTAINER Alexander Turcic "alex@zeitgeist.se"  
# Install dependencies.  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
git \  
dnsutils \  
bsdmainutils && \  
git clone https://github.com/drwetter/testssl.sh && \  
apt-get -y purge git && \  
apt-get -y autoremove --purge && \  
rm -rf /var/lib/apt/lists/*  
  
ENV TERM xterm-256color  
  
RUN \  
export uid=1000 gid=1000 && \  
groupadd --gid ${gid} user && \  
useradd --uid ${uid} \--gid ${gid} \--create-home user  
  
USER user  
WORKDIR /testssl.sh  
  
ENTRYPOINT ["/testssl.sh/testssl.sh"]  
CMD ["--help"]  

