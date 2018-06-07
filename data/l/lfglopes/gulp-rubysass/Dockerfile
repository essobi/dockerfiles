FROM node:8  
MAINTAINER Luis Lopes  
  
RUN apt-get update  
RUN apt-get install -y locales ruby-sass  
  
RUN locale-gen "en_US.UTF-8"  
ENV LC_CTYPE=en_US.UTF-8  
  
RUN npm install yarn -g  
RUN yarn global add gulp-cli@1.4.0  
  
#RUN yarn global add bower@1.7.9 -g  

