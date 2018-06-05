# We use Ubuntu 12.04 (precise) as our base image due to problems with Xvfb in  
# Docker on Ubuntu 14.04 (trusty)  
FROM ubuntu:precise  
MAINTAINER Vlad Korolev, LLC  
  
ENV NODE_VERSION stable  
ENV PATH /usr/local/bin:$PATH  
  
# Install build dependencies for Nave  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
build-essential \  
python \  
curl \  
git \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y python-software-
properties \  
&& DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:fkrull/deadsnakes-
python2.7 \  
&& DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:ubuntu-
toolchain-r/test \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y upgrade python \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install gcc-4.8 \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install g++-4.8 \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install pkg-config \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install libfreetype6 \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install libfontconfig \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install libcairo2-dev \  
&& update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 50 \  
&& update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 50 \  
&& DEBIAN_FRONTEND=noninteractive rm -rf /var/lib/apt/lists/*  
  
# Install Nave  
RUN curl -f -o /usr/local/bin/nave
https://raw.githubusercontent.com/isaacs/nave/master/nave.sh  
RUN chmod a+x /usr/local/bin/nave  
  
# Build/install NodeJS  
RUN nave usemain $NODE_VERSION  
  
# Install phantomJS as global. It doesn't like to be installed in local  
# direcotry when it's running on Mac through docker-machine  
RUN npm install -g phantomjs  
  
# Install global components  
RUN npm install -g bower gulp  
  
RUN adduser --uid 1000 --ingroup adm --disabled-password --gecos '' builder \  
&& adduser --uid 498 --ingroup adm --disabled-password --gecos '' go \  
&& adduser --uid 500 --ingroup adm --disabled-password --gecos '' ec2-user  

