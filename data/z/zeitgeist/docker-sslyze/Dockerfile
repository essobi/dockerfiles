# vim:set ft=dockerfile:  
# VERSION 1.0  
# AUTHOR: Alexander Turcic <alex@zeitgeist.se>  
# DESCRIPTION: sslyze in a Docker container  
# TO_BUILD: docker build --rm -t zeitgeist/docker-sslyze .  
# SOURCE: https://github.com/alexzeitgeist/docker-sslyze  
# Pull base image.  
FROM debian:jessie  
MAINTAINER Alexander Turcic "alex@zeitgeist.se"  
ENV RELEASE_URL https://github.com/nabla-c0d3/sslyze/archive/0.13.3.zip  
ENV RELEASE_DIR /sslyze-0.13.3  
# Compile sslyze  
RUN \  
apt-get update && \  
apt-get install -y python2.7 unzip wget python-pip python-dev gcc --no-
install-recommends && \  
wget "${RELEASE_URL}" -O sslyze.zip && \  
unzip sslyze.zip && \  
rm sslyze.zip && \  
cd ${RELEASE_DIR} && \  
pip install -r requirements.txt --target ./lib && \  
apt-get -y purge unzip wget python-pip python-dev gcc && \  
apt-get -y autoremove --purge && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
export uid=1000 gid=1000 && \  
groupadd --gid ${gid} user && \  
useradd --uid ${uid} \--gid ${gid} \--create-home user  
  
USER user  
WORKDIR ${RELEASE_DIR}  
  
ENTRYPOINT ["/usr/bin/python2.7", "sslyze_cli.py"]  
CMD ["-h"]  

