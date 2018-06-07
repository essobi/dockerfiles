FROM node:6  
EXPOSE 8080  
MAINTAINER Christopher S. Case <chris.case@g33xnexus.com>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ADD . /usr/src/app/  
  
RUN npm install \  
&& npm install grunt-cli \  
&& npm install bower \  
&& ./node_modules/.bin/bower install --allow-root \  
&& ./node_modules/.bin/grunt build  
  
ARG PORTAL_API_KEY  
  
CMD [ "node", "server.js" ]  

