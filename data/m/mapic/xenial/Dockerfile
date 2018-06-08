##  
# mapic/xenial:latest  
#  
FROM ubuntu:xenial  
MAINTAINER knutole@mapic.io  
  
# upgrade ubuntu  
RUN apt-get update --fix-missing -y  
RUN apt-get install software-properties-common -y  
RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y  
RUN apt-get update --fix-missing -y  
RUN apt-get upgrade -y  
RUN apt-get dist-upgrade -y  
  
# install basics  
RUN apt-get update -y  
RUN apt-get install -y \  
wget fish htop curl zip git sudo \  
unzip bmon nmon nmap pigz make \  
python-software-properties \  
apt-transport-https \  
protobuf-compiler \  
libprotobuf-dev \  
build-essential \  
redis-tools \  
subversion \  
mlocate  
  
# ensure everything up to date  
RUN apt-get update --fix-missing -y  
  
# install node-js  
ADD ./install-nodejs.sh /tmp/  
RUN sh /tmp/install-nodejs.sh  
  
# set node path  
ENV NODE_PATH /usr/local/lib/node_modules  
  
# install node deps  
RUN npm install -g grunt-cli  
RUN npm install -g grunt  
RUN npm install -g nodemon  
RUN npm install -g forever  
RUN npm install -g mocha  
RUN npm install -g node-pre-gyp  
RUN npm install -g npm-check-updates  
RUN npm install -g karma  
RUN npm install -g topojson  
RUN npm install -g yarn  
  
# set terminal  
ENV TERM xterm  
  
# entrypoint  
CMD ['bash']

