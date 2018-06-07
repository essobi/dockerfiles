FROM ubuntu:14.04.2  
MAINTAINER Stephan Buys <stephan.buys@panoptix.co.za>  
  
ENV REFRESHED_ON "18 Aug 2015"  
RUN apt-get update && \  
apt-get -y install \  
curl \  
git \  
ldap-utils \  
python-jinja2 \  
python-pip \  
python-yaml \  
python-software-properties \  
software-properties-common  
  
#install ldap (for the slapdpasswd util)  
RUN apt-get -y install slapd  
  
#install Docker  
RUN curl -sSL https://get.docker.com/ | sudo sh  
  
#install Docker Compose  
RUN curl -L https://github.com/docker/compose/releases/download/1.5.1/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
#install Docker Machine  
RUN curl -L https://github.com/docker/machine/releases/download/v0.5.2/docker-
machine_linux-amd64 > /usr/local/bin/docker-machine && \  
chmod +x /usr/local/bin/docker-machine  
  
ADD . /hotrod  
WORKDIR /hotrod  
  
#install the mini template script  
RUN cd /tmp && git clone https://github.com/panoptix-za/mini-templates.git &&
\  
ln -sf /tmp/mini-templates/mini.py /usr/local/bin/mini.py  
  
CMD /bin/bash  
  

