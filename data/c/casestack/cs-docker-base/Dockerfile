# use docker base image https://github.com/phusion/baseimage-docker  
FROM phusion/baseimage:0.9.17  
MAINTAINER CaseStack <cloudservices@casestack.com>  
  
# Set correct environment variables.  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Install Dependencies  
RUN apt-get -qqy update  
RUN apt-get -qqy install wget unzip figlet curl dnsutils htop screen  
RUN apt-get -qqy install git software-properties-common build-essential gcc
make cmake graphicsmagick  
  
# Install Required PPAs  
RUN add-apt-repository -y ppa:openjdk-r/ppa  
RUN apt-add-repository -y ppa:brightbox/ruby-ng  
RUN apt-add-repository -y ppa:nginx/stable  
RUN apt-get -qqy update  
  
# Install Java  
RUN apt-get -qqy install openjdk-8-jdk  
RUN apt-get -qqy install maven  
  
# Install Python  
RUN apt-get -qqy install python  
  
# Install Ruby  
RUN apt-get -qqy install ruby-dev  
  
# Install Node 4  
# https://github.com/nodesource/distributions  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -  
RUN sudo apt-get install -y nodejs  
RUN npm install -g npm  
RUN npm install -g node-gyp  
RUN npm install -g bunyan  
RUN npm install -g npm-check-updates  
RUN npm install -g jsdoc  
RUN npm install -g nodemon  
RUN npm install -g eslint  
RUN npm install -g eslint-plugin-angular  
  
# Install Nginx  
RUN apt-get -qqy install nginx-extras  
  
# Install Lua & Dependencies  
RUN apt-get -qqy install libssl-dev libcurl3-dev lua5.1 luarocks
libluajit-5.1-dev luajit  
RUN apt-get -qqy install lua-nginx-redis  

