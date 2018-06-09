# VERSION 1.0  
# AUTHOR: Jerome Guibert <jguibert@gmail.com>  
# DESCRIPTION: Thumbd image based on debian:node  
# TO_BUILD: docker build --rm -t airdock/thumbd .  
# SOURCE: https://github.com/airdock-io/docker-thumbd  
FROM airdock/node:10  
MAINTAINER Jerome Guibert <jguibert@gmail.com>  
# Install Thumbd  
RUN apt-get update -qq && apt-get install -y --no-install-recommends
imagemagick && \  
mkdir -p /srv/node/thumbd && cd /srv/node/thumbd && \  
npm install nan && npm install thumbd && npm cache clear && \  
chown -R node:node /srv/node && \  
/root/post-install  
  
WORKDIR /srv/node/thumbd  
  
CMD ["gosu", "node:node", "npm", "start", "thumbd"]  

