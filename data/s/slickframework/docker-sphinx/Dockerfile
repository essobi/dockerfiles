FROM ubuntu:16.04  
MAINTAINER Filipe Silva <silvam.filipe@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# System update  
RUN apt-get update && apt-get upgrade -y  
  
# Intall python-sphinx  
RUN apt-get install curl python-sphinx python-setuptools python-dev build-
essential -y  
  
RUN easy_install pip  
  
RUN pip install sphinx-autobuild sphinxcontrib-phpdomain  
  
# Create the user sphinx  
RUN useradd -ms /bin/bash -d /docs sphinx  
  
# Grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& curl -sSLo /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& curl -sSLo /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
WORKDIR /docs

