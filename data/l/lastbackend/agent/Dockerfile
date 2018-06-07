# Last.Backend API image  
FROM node:5-wheezy  
  
MAINTAINER Last.Backend Team <team@lastbackend.com>  
  
ENV NODE_ENV production  
  
ENV PROXY_HOST logs.lastbackend.com  
ENV PROXY_PORT 2968  
ENV DOCKER_SOCK /docker.sock  
ENV DATABASE /var/  
  
ENV DEBUG lb:*  
  
ADD . /opt  
  
WORKDIR /opt  
  
RUN rm -rf node_modules  
RUN npm install  
  
VOLUME /opt  
  
CMD node src/app.js  

