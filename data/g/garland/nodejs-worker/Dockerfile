#  
# Node.js Dockerfile  
#  
#  
# Pull base image.  
FROM dockerfile/ubuntu  
  
# Install Node.js  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get install -y nodejs  
  
# Setup AutDevBot's App  
RUN cd /opt; git clone
https://2315b2902537ff5da7fa205d5ebd0aab0114a9ba@github.com/sekka1/AutoDevBotContainerNodes.git  
RUN cd /opt/AutoDevBotContainerNodes; npm install  
RUN npm install -g jasmine-node

