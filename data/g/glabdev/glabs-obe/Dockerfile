#####################################################  
# Dockerfile to build NodeJS container Images  
# Based on Ubuntu  
# Secret Sauce for Gattaca  
####################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu  
  
# File Author / Maintainer  
MAINTAINER Gattaca2  
  
# Create User app  
RUN useradd -ms /bin/bash app  
  
# Modify uid of user app  
RUN usermod -u 1100 app  
  
# Modify gid of group app  
RUN groupmod -g 1100 app  
  
  
######################## create user to run nodejs  
  
RUN useradd -ms /bin/bash nodejs  
RUN usermod -u 9002 nodejs  
RUN groupmod -g 9002 nodejs  
  
# insert nodejs group to app  
  
RUN usermod -aG app nodejs  
  
# Update the repository source list  
RUN apt-get update  
  
# Install Build Essential for compiling  
RUN apt-get install -y build-essential  
  
# install dependencies  
RUN apt-get install -y python libkrb5-dev graphicsmagick  
  
# Install Curl for get nodeJS  
RUN apt-get install -y curl  
  
# Add NodeJS to /tmp/  
ADD https://nodejs.org/dist/v6.2.1/node-v6.2.1-linux-x64.tar.xz /opt/  
  
RUN cd /opt/;tar xf node-v6.2.1-linux-x64.tar.xz  
  
RUN ls /opt  
  
# Rename nodejs folder become more simplified  
RUN mv /opt/node-v6.2.1-linux-x64 /opt/nodejs6  
  
# Set path for nodejs  
RUN ln -s /opt/nodejs6/bin/node /usr/local/bin/node  
RUN ln -s /opt/nodejs6/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm  
RUN ln -s /opt/nodejs6/lib/node_modules/forever/bin/forever
/usr/local/bin/forever  
  
# Cleanup cache and installation  
RUN rm /opt/node-v6.2.1-linux-x64.tar.xz  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# change the default working directory  
VOLUME /opt/apps/  
#VOLUME /opt/apps/node_modules  
  
WORKDIR /opt/apps  
  
# Install forever as global  
RUN npm install forever@0.14.1 -g  
RUN npm install sequelize-cli -g  
  
RUN ln -s /opt/nodejs6/bin/sequelize /usr/local/bin/sequelize  
  
# Set the HOME env to /home/app  
ENV HOME /home/app  
  
# set UID to be used when images is running  
USER 9002  
  
EXPOSE 3000  

