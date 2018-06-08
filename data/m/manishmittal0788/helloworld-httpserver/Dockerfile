FROM ubuntu:latest  
MAINTAINER Manish Mittal  
  
RUN apt-get update  
RUN apt-get install -y nodejs  
RUN apt-get install -y npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN npm install -g http-server  
  
ADD HelloWorld.html /usr/apps/hello-docker/HelloWorld.html  
WORKDIR /usr/apps/hello-docker/  
  
CMD ["http-server", "-s"]

