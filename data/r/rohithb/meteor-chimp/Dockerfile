FROM openjdk:7-jdk  
  
MAINTAINER Rohith Bhaskaran  
  
RUN apt-get update  
RUN apt-get install -y build-essential  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install chimp selenium-standalone -g -q &&selenium-standalone install
--version=2.48.2 --baseURL=https://selenium-release.storage.googleapis.com  
  
RUN mkdir -p /usr/lib/node_modules/chimp/node_modules/selenium-
standalone/.selenium/selenium-server/  
RUN cp /usr/lib/node_modules/selenium-standalone/.selenium/selenium-
server/2.48.2-server.jar /usr/lib/node_modules/chimp/node_modules/selenium-
standalone/.selenium/selenium-server/  
  
RUN curl https://install.meteor.com/ | sh  
  
RUN apt-get install -y locales  
RUN locale-gen en_US.UTF-8  
RUN localedef -i en_GB -f UTF-8 en_US.UTF-8

