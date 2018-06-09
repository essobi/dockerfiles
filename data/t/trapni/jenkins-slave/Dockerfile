FROM ubuntu:16.04  
MAINTAINER Infra <infrateam@dawanda.com>  
  
RUN apt-get update \  
&& apt-get -y install locales openjdk-8-jre-headless git wget make curl wget
ca-certificates  
  
RUN locale-gen en_US.utf8  
ENV LANG=en_US.utf8 LC_ALL=en_US.utf8  
  
RUN wget -O /usr/local/bin/docker
https://get.docker.com/builds/Linux/x86_64/docker-1.10.0 \  
&& chmod +x /usr/local/bin/docker  
  
RUN wget -O /usr/local/bin/docker-compose
https://github.com/docker/compose/releases/download/1.7.1/docker-compose-
Linux-x86_64 \  
&& chmod +x /usr/local/bin/docker-compose  
  
ENV RUBY_VERSION=2.3.0  
RUN apt-get -y install build-essential \  
libffi-dev \  
libgdbm-dev \  
libncurses5-dev \  
libreadline-dev \  
libssl-dev \  
libyaml-dev \  
zlib1g-dev \  
libxml2-dev \  
libxslt-dev \  
curl \  
wget \  
git \  
libjansson-dev \  
libmysqlclient-dev \  
libhiredis-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
imagemagick \  
nodejs \  
vim \  
ca-certificates \  
zip  
  
RUN curl -L -o /tmp/ruby-build.tar.gz \  
https://github.com/sstephenson/ruby-build/archive/master.tar.gz \  
&& cd /tmp \  
&& tar -xvzf ruby-build.tar.gz \  
&& cd ruby-build-master \  
&& ./install.sh \  
&& ruby-build $RUBY_VERSION /opt/$RUBY_VERSION \  
&& rm -rf /tmp/ruby-build-master /tmp/ruby-build.tar.gz ruby-build*.log  
  
ENV GEM_HOME=/usr/local/bundle \  
PATH=/usr/local/bundle/bin:/opt/$RUBY_VERSION/bin:$PATH  
  
RUN mkdir -p /opt/jenkins  
WORKDIR /opt/jenkins/  
ADD run-agent /  
RUN wget https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/2.2/swarm-client-2.2-jar-with-dependencies.jar  
  
ENV JENKINS_MASTER http://rack5-compute3:10015/  
  
CMD ["/run-agent"]  

