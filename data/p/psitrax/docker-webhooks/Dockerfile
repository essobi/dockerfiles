FROM mhart/alpine-node:latest  
MAINTAINER Christoph Wiechert <wio@psitrax.de>  
  
WORKDIR /root  
RUN npm install docker-webhooks  
  
EXPOSE 3000  
CMD ["/usr/bin/node", "/root/node_modules/docker-webhooks/app.js"]

