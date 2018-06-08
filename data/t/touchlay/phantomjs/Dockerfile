FROM node:latest  
  
RUN apt-get -yq update && \  
apt-get -yqq install git && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm install phantomjs-prebuilt  

