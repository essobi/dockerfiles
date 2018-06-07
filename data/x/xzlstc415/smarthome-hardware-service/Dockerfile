# Create image from nodejs official base image  
#FROM node:6.10.3-alpine  
FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get clean  
RUN apt-get update  
RUN apt-get -qq update  
RUN apt-get install -y sudo  
RUN apt-get install -y curl  
RUN sudo apt-get install -y python-software-properties  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
# fucking debian installs `node` as `nodejs`  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
  
#we need java and openssl for certificate generation  
RUN apt-get install -y openjdk-8-jdk  
RUN apt-get install -y openjdk-8-jre  
RUN apt-get install -y expect  
  
# Make dir  
RUN mkdir -p home/node/hub6-app  
  
# Environment variables  
ENV SHELL=/bin/bash  
ENV HOME=/home/node  
ENV NODE_HOST=localhost  
  
  
# Copy files  
COPY npm-shrinkwrap.json $HOME/hub6-app  
COPY keystores/local_policy.jar /usr/lib/jvm/java-8-openjdk-
amd64/jre/lib/security/  
COPY keystores/US_export_policy.jar /usr/lib/jvm/java-8-openjdk-
amd64/jre/lib/security/  
COPY . $HOME/hub6-app/  
  
# Set permissions  
#RUN chown -R node:node $HOME/*  
# Set working dir  
WORKDIR $HOME/hub6-app  
  
# Install dependencies  
RUN npm install node-gyp -g  
RUN apt-get install -y python  
RUN apt-get install -y make  
RUN apt-get -qq update && apt-get install -y g++  
RUN npm install  
RUN npm rebuild bcrypt --build-from-source  
  
# Port  
EXPOSE 8000  
# Set user  
#User node  
# Start Nodejs  
CMD ["autoexpect"]  
CMD ["node", "index.js"]  

