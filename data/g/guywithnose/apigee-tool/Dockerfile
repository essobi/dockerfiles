FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y git-core python php5-cli php5-curl
npm nodejs  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN git clone https://github.com/apigee/api-platform-tools.git  
  
WORKDIR /api-platform-tools  
  
RUN python setup.py install  
  
VOLUME /code  
WORKDIR /code  

