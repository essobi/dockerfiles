# Drupal Dockerfile Config  
FROM node:6  
MAINTAINER Kerry Knopp <kerry@codekoalas.com>  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update \  
&& apt-get install -y git cron yarn vim --no-install-recommends && rm -rf
/var/lib/apt/lists/*  
  
# Predefine ENV  
ENV NODE_START="server.js"  
# Add files.  
ADD node-start /node-start  
ADD ssmtp.conf /etc/ssmtp/ssmtp.conf  
ADD crons.conf /root/crons.conf  
ADD post-merge /post-merge  
  
# Install pm2  
RUN npm install -g pm2 bower  
  
WORKDIR /usr/src/app  
  
CMD ["bash" , "/node-start"]  

