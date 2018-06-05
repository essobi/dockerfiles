# Docker file for Angular ESPN API App  
# Ubuntu setup graciously borrowed from Oskar Hane  
# http://oskarhane.com/create-a-nodejs-docker-io-image/  
# DOCKER-VERSION 1.0  
#1 Base image  
FROM ubuntu:12.10  
  
#2 Who?  
MAINTAINER scott elson, aguyawry@gmail.com  
  
#3 Do some updates!  
RUN apt-get -y update && apt-get -y upgrade  
  
#4 Install some packages we need  
RUN apt-get -y install python-software-properties python g++ make software-
properties-common  
  
#5 Add node repository to sources.list and update apt  
RUN add-apt-repository -y ppa:chris-lea/node.js && apt-get update  
  
#6 Install node.js and npm  
RUN apt-get -y install nodejs  
  
#7 Test them  
RUN node -v;npm -v  
  
#8 Fresh!  
RUN npm cache clean  
  
#9 Add the app files  
ADD . /src  
  
#10 Install app dependencies  
RUN npm install /src  
  
#11 Port  
EXPOSE 8002  
  
#12 Start the server  
#CMD ["npm", "start"]  
CMD ["npm", "http-server -p 8002"]  

