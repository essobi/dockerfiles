FROM ubuntu:14.04  
MAINTAINER PauloWhyte  
  
# Installation:  
# Import MongoDB public GPG key AND create a MongoDB list file  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list  
# Update apt-get sources AND install MongoDB  
RUN apt-get update && apt-get install -y mongodb-org-shell=3.0.7 mongodb-org-
tools=3.0.7  
  

