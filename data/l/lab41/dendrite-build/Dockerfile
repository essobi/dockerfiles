from ubuntu:precise  
MAINTAINER Charlie Lewis <charliel@lab41.org>  
  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update --fix-missing; \  
apt-get install -y python-software-properties; \  
apt-add-repository ppa:chris-lea/node.js; \  
apt-get update; \  
apt-get install -y -q build-essential \  
bzip2 \  
cmake \  
curl \  
default-jdk \  
dpkg \  
gcc \  
git \  
g++ \  
gnuplot \  
make \  
maven \  
nodejs \  
rsyslog \  
supervisor \  
tomcat7 \  
wget \  
zlib1g-dev; \  
apt-get clean  

