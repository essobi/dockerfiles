FROM alpine:3.3  
MAINTAINER Paul Fremantle (paul@fremantle.org)  
  
RUN apk --update add nodejs && \  
ln -s /usr/bin/nodejs /usr/local/bin/node && \  
npm install express && \  
npm install -g forever && \  
mkdir -p /home/root/js  
  
ADD simpletest.js /home/root/js  
EXPOSE 8080  
ENTRYPOINT forever /home/root/js/simpletest.js  
  

