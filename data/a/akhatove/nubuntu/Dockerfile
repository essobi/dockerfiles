FROM ubuntu:14.04  
MAINTAINER RA  
# Vim  
CMD "/bin/bash"  
RUN apt-get update && apt-get install -y vim  
# Git  
CMD "/bin/bash"  
RUN apt-get update && apt-get install -y --no-install-recommends dialog apt-
utils ssh curl wget && rm -rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install -y python-software-properties software-
properties-common  
RUN add-apt-repository ppa:git-core/ppa -y  
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf
/var/lib/apt/lists/*  
  
# Node.js  
CMD "/bin/bash"  
RUN curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -  
RUN apt-get update && apt-get install -y nodejs  
  
# MongoDB  
CMD "/bin/bash"  
RUN groupadd -r mongodb && useradd -r -g mongodb mongodb  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2
multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
RUN apt-get update && apt-get install -y mongodb-org

