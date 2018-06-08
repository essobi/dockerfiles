# Drupal Dockerfile Config  
FROM node:8  
MAINTAINER Kerry Knopp <kerry@codekoalas.com>  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update \  
&& apt-get install -y git cron yarn vim --no-install-recommends && rm -rf
/var/lib/apt/lists/*  
  
# Predefine ENV  
ENV NODE_START="pm2 start --no-daemon server.js --watch"  
ENV NPM_CONFIG_LOGLEVEL warn  
  
# Add files.  
ADD node-start /node-start  
ADD ssmtp.conf /etc/ssmtp/ssmtp.conf  
ADD crons.conf /root/crons.conf  
ADD post-merge /root/post-merge  
  
# Install pm2  
RUN npm install -g pm2 bower  
  
WORKDIR /usr/src/app  
  
CMD ["bash" , "/node-start"]  

