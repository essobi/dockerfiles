# vim:set ft=dockerfile:  
# VERSION 1.0  
# AUTHOR: Alexander Turcic <alex@zeitgeist.se>  
# DESCRIPTION: cli53 in a Docker container  
# TO_BUILD: docker build --rm -t zeitgeist/docker-cli53 .  
# SOURCE: https://github.com/alexzeitgeist/docker-cli53  
# Pull base image.  
FROM debian:jessie  
MAINTAINER Alexander Turcic "alex@zeitgeist.se"  
# Install dependencies.  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
git \  
python-dnspython \  
python-setuptools \  
python2.7 && \  
git clone https://github.com/barnybug/cli53.git && \  
cd cli53 && \  
python setup.py build && \  
python setup.py install && \  
cd .. && \  
rm -rf cli53 && \  
apt-get -y purge git && \  
apt-get -y autoremove --purge && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
export uid=1000 gid=1000 && \  
groupadd --gid ${gid} user && \  
useradd --uid ${uid} \--gid ${gid} \--create-home user  
  
USER user  
WORKDIR /home/user  
  
ENTRYPOINT ["/usr/local/bin/cli53"]  
CMD ["-?"]

