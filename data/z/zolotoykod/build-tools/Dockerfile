FROM phusion/baseimage:latest  
LABEL maintainer="Constantine Karnaukhov <genteelknight@gmail.com>"  
  
# Let's start with some basic stuff.  
RUN apt-get update -qq \  
&& apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
lxc \  
iptables \  
make \  
git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Docker from Docker Inc. repositories.  
RUN curl -sSL https://get.docker.com/ | sh  
  
# Install docker-compose  
RUN curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  
  
# Install shipit binary  
RUN SHPT=/usr/local/bin/shipit && curl -o $SHPT
https://raw.githubusercontent.com/sapegin/shipit/master/bin/shipit && chmod +x
$SHPT && unset SHPT  

