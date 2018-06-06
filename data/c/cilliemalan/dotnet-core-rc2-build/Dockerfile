FROM ubuntu:14.04  
  
MAINTAINER Cillie Malan <cilliemalan@gmail.com>  
  
# main deps  
RUN apt-get update -qq && apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup_5.x | bash - && \  
apt-get update -qq && \  
apt-get install -y -qq unzip curl libunwind8 gettext libssl-dev
libcurl4-openssl-dev zlib1g libicu-dev uuid-dev git build-essential && \  
apt-get install -y -qq nodejs && \  
npm install -g npm  
  
  
# some general npm deps  
RUN ["/bin/bash", "-c", "npm install -g -y typings bower grunt-cli gulp-cli
mocha typescript node-gyp"]  
  
# dotnet core  
RUN sh -c 'echo "deb [arch=amd64] https://apt-
mo.trafficmanager.net/repos/dotnet/ trusty main" >
/etc/apt/sources.list.d/dotnetdev.list' && \  
apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893 && \  
apt-get update && \  
apt-get install -y -qq dotnet-dev-1.0.0-preview1-002702  

