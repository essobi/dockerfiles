FROM node:6  
MAINTAINER Massimo Schiavon <massimo@themostaza.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update -qq && \  
apt-get install -qy curl apt-transport-https  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update -qq && \  
apt-get install -qy yarn libelf1 jq rsync  
  
WORKDIR /workspace

