from node:slim  
  
MAINTAINER Rousseau L. Braga rbraga@nuxman.com.br  
  
RUN apt-get update && apt-get install -y git  
  
RUN npm install -g sails grunt kerberos bower pm2 npm-check-updates sails-
mongo  
  
RUN mkdir -p /usr/src/app  
  
VOLUME ["/usr/src/app"]  
  
WORKDIR /usr/src/app  
  
EXPOSE 1337  

