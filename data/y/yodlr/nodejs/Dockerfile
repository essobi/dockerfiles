FROM debian:jessie  
MAINTAINER Ross Kukulinski "ross@getyodlr.com"  
  
ENV LAST_UPDATED 4_29_2015  
  
RUN apt-get -qq update && \  
apt-get -yqq install apt-transport-https && \  
apt-get -qq install -y \  
python-software-properties \  
software-properties-common \  
curl \  
wget \  
git \  
build-essential \  
supervisor && \  
curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add \-
&& \  
echo 'deb https://deb.nodesource.com/node_0.10 jessie main' >
/etc/apt/sources.list.d/nodesource.list && \  
echo 'deb-src https://deb.nodesource.com/node_0.10 jessie main' >>
/etc/apt/sources.list.d/nodesource.list && \  
apt-get -qq update && \  
apt-get -qq install -y nodejs && \  
npm -g install npm && \  
npm -g install \  
bower \  
gulp \  
grunt-cli \  
bunyan \  
&& \  
mkdir -p /var/log/supervisor && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/usr/bin/node", "--version"]  

