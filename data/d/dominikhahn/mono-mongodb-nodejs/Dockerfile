# Pull base image.  
FROM mono:latest  
  
MAINTAINER Dominik Hahn <dominik@monostream.com>  
  
# Set ARG/ENV  
ARG DEBIAN_FRONTEND  
ENV DEBIAN_FRONTEND noninteractive  
  
## Install SW  
### Install MongoDB  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 && \  
echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \  
apt-get -yqq update && \  
apt-get install -yqq mongodb-org  
  
### Install NodeJS/NPM  
RUN curl -sL https://deb.nodesource.com/setup | bash - && \  
apt-get install -yqq nodejs build-essential  
  
# Executing defaults  
CMD [ "/bin/bash" ]  

