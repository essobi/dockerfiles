FROM ubuntu:trusty  
RUN apt-get update && apt-get install -y curl jq  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
RUN apt-get install -y nodejs && \  
npm install -g n  
  
# First, build the product in a temp folder  
ONBUILD COPY *.json /opt/build/  
ONBUILD WORKDIR /opt/build  
ONBUILD RUN n `jq -r .engines.node package.json` && \  
npm update -g npm && \  
npm install  
ONBUILD COPY ./ /opt/build  
  
ONBUILD CMD npm test

