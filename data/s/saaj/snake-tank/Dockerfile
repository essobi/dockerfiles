FROM ubuntu:xenial  
  
MAINTAINER saaj <mail@saaj.me>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN set -ex; \  
apt-get update; \  
apt-get install --yes \--no-install-recommends software-properties-common; \  
add-apt-repository ppa:deadsnakes/ppa; \  
add-apt-repository ppa:pypy/ppa; \  
apt-get update; \  
apt-get install --yes \--no-install-recommends \  
build-essential libffi-dev libssl-dev \  
python-tox python-pip python3-pip \  
python2.7 python2.7-dev \  
python3.4 python3.4-dev \  
python3.5 python3.5-dev \  
python3.6 python3.6-dev \  
pypy pypy-dev; \  
apt-get purge -y --auto-remove software-properties-common; \  
rm -rf /var/lib/apt/lists/*  
  
RUN set -ex; \  
apt-get update; \  
apt-get install --yes \--no-install-recommends wget; \  
wget -q -P /tmp
https://bitbucket.org/pypy/pypy/downloads/pypy3-v5.10.1-linux64.tar.bz2; \  
tar -x -C /opt -f /tmp/pypy3-v5.10.1-linux64.tar.bz2; \  
rm /tmp/pypy3-v5.10.1-linux64.tar.bz2; \  
mv /opt/pypy3-v5.10.1-linux64 /opt/pypy3; \  
ln -s /opt/pypy3/bin/pypy3 /usr/local/bin/pypy3; \  
apt-get purge -y --auto-remove wget; \  
rm -rf /var/lib/apt/lists/*  

