# Set the base image to Ubuntu  
FROM ubuntu:latest  
  
# File Author / Email  
MAINTAINER Eric Koh <EricKoh.dev@gmail.com>  
  
# Install Node.js and other dependencies  
RUN apt-get update && \  
apt-get -y install curl && \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get -y install nodejs  
#RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
# Install yarn  
#RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
#RUN apt-get update && apt-get -y install yarn  
# Install pm2  
RUN npm install pm2 -g  
  
# Provides cached layer for node_modules  
COPY package.json /tmp/  
RUN cd /tmp && npm install  
  
# Define working directory  
RUN mkdir -p /usr/src/app  
RUN cp -a /tmp/node_modules /usr/src/app/  
  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
  
ARG env  
RUN if [ "$env" != "development" ]; then npm run build; fi  
  
# Expose port  
EXPOSE 8080  
CMD if [ "$NODE_ENV" = "production" ]; then pm2-docker start
ecosystem.config.js; else pm2-dev start ecosystem.config.js; fi  

