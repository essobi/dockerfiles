############################################################  
#  
# Dockerfile to build an Ubuntu container images and install  
# requirements for building libdrizzle-redux  
#  
# For more info:  
# https://github.com/sociomantic-tsunami/libdrizzle-redux  
#  
# docker build -f Dockerfile .  
#  
############################################################  
FROM ubuntu:trusty  
MAINTAINER Andreas Bok Andersen <andreas.bok@sociomantic.com>  
  
WORKDIR /root  
  
## Setting environment variables required for running tests  
ENV MYSQL_SERVER=127.0.0.1 \  
MYSQL_PASSWORD='root' \  
MYSQL_USER=root \  
SKIP_TEST_ON_ERROR=0  
ENV DEBIAN_FRONTEND noninteractive  
  
# delete all the apt list files since they're big and get stale quickly  
RUN rm -rf /var/lib/apt/lists/*  
# this forces "apt-get update" in dependent images, which is also good  
# enable the universe  
RUN sed -i 's/^#\s*\\(deb.*universe\\)$/\1/g' /etc/apt/sources.list  
  
RUN apt-get update -y && \  
apt-get -y upgrade && \  
apt-get -y install \  
git openssh-client autoconf libtool g++ gcc make zlib1g-dev debconf-utils ca-
certificates  
RUN mkdir -p /root/.ssh  
RUN ssh-keygen -q -t rsa -N '' -f /root/.ssh/id_rsa  
RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config  
  
RUN rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
# rm -rf /var/tmp/* && \  
# rm -rf /var/lib/apt/lists/*  
# clone libdrizzle-redux repository  
RUN ls -la /etc/ssl/certs/  
RUN cd ~ && \  
git clone https://github.com/sociomantic-tsunami/libdrizzle-redux.git  
WORKDIR libdrizzle-redux  
  
# RUN ./bootstrap.sh &&\  

