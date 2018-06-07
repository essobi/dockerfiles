FROM ubuntu:14.04  
MAINTAINER Vinicius Souza <hi@vsouza.com>  
  
RUN apt-get update  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo bash -  
RUN apt-get -y install nodejs  
RUN apt-get -y install build-essential  
RUN apt-get -y install git  
RUN npm install -g git+https://github.com/virtyx-technologies/kinesalite.git  
  
EXPOSE 4567  
ENTRYPOINT ["/usr/bin/kinesalite"]  

