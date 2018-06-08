FROM ubuntu:16.04  
MAINTAINER Suleyman Yildirim <suleymanube@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y nodejs npm  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/  
  
# Cache is used here  
WORKDIR /opt/app  
ADD . /opt/app  
  
EXPOSE 80  
CMD [ "npm", "start" ]

