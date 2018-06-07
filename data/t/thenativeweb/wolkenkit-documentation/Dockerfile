FROM thenativeweb/wolkenkit-box-node:1.2.0  
MAINTAINER the native web <hello@thenativeweb.io>  
  
ADD . /documentation/  
  
WORKDIR /documentation  
  
RUN npm install --production --silent  
  
CMD [ "dumb-init", "node", "app.js" ]  

