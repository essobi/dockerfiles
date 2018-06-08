# Based on https://github.com/saltstack/docker-containers  
  
FROM debian:wheezy  
MAINTAINER Arnold Bechtoldt <mail@arnoldbechtoldt.com>  
  
RUN apt-get update -qq  
  
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -yV -o
DPkg::Options::=--force-confold wget && \  
# wget -q -O- "http://debian.saltstack.com/debian-salt-team-joehealy.gpg.key"
| apt-key add - && \  
# echo "deb http://debian.saltstack.com/debian wheezy-saltstack main" >
/etc/apt/sources.list.d/saltstack.list  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get upgrade -yV -o
DPkg::Options::=--force-confold  
  
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -yV -o
DPkg::Options::=--force-confold \  
# apt-transport-https \  
# apt-utils \  
# curl \  
# msgpack-python \  
# psutils \  
# procps \  
# python \  
# python-crypto \  
# python-jinja2 \  
# python-m2crypto \  
# python-requests \  
# python-software-properties \  
# python-yaml \  
# python-zmq \  
# software-properties-common \  
# virt-what  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yV -o
DPkg::Options::=--force-confold \  
curl \  
psutils \  
procps \  
python \  
python-apt \  
tree \  
virt-what \  
wget  
  
RUN apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

