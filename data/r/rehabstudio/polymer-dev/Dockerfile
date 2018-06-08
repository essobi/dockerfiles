FROM debian  
MAINTAINER Ryan Grieve <ryan@rehabstudio.com>  
  
# update, upgrade and install base requisites  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y build-essential git curl  
  
# install node from ppa  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -y nodejs  
  
# npm-ception: install latest from npm  
RUN npm install -g npm  
  
# install global tools  
RUN npm install -g \  
bower \  
gulp \  
vulcanize \  
crisper \  
polylint \  
polyclean \  
polybuild  
  
RUN mkdir /src  
RUN mkdir /src/node_modules  
  
ADD assets/package.json /src/  
RUN cd /src; npm install  
  
VOLUME ["/src/node_modules"]  
WORKDIR /src  

