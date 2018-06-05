# use the nodejs base image provided by docker  
FROM dockerfile/nodejs  
MAINTAINER Matthew L. Livingston, matt.l.livingston@gmail.com  
  
# make sure the package repo is up to date  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get upgrade  
RUN apt-get update  
  
# Get Git  
RUN apt-get install git-core  
  
# Update npm and install node packages  
RUN npm -g update npm  
RUN npm install -g express  
RUN npm install -g forever  
RUN npm install -g bower  
RUN npm install -g brunch  
  
RUN mkdir /var/www

