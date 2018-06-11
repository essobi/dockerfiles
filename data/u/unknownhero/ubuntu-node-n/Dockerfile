FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install -q -y --force-yes --fix-missing build-
essential libpq-dev git curl wget g++ python  
  
RUN mkdir ~/tmp && \  
cd ~/tmp && \  
git clone https://github.com/visionmedia/n && \  
cd n && \  
make install && \  
n stable && \  
npm install -g node-gyp grunt grunt-cli bower node-inspector  

