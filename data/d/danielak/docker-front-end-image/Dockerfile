FROM node:8.9.3  
LABEL author="Brian A. Danielak"  
LABEL version="0.1"  
  
# Environment Variables  
# Install some basic infrastructure  
RUN apt-get update  
RUN apt-get install --assume-yes ca-certificates  
RUN apt-get install --assume-yes mysql-client  
  
# Install yarn  
RUN apt-get install apt-transport-https  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install yarn  

