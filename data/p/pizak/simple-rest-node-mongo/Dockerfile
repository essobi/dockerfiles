FROM alpine:3.3  
RUN apk --update add nodejs && \  
ln -s /usr/bin/nodejs /usr/local/bin/node && \  
npm install express uuid mongoose && \  
npm install -g forever && \  
mkdir -p /home/root/js  
  
ADD src/*.js /home/root/js/  
EXPOSE 8000  
RUN node /home/root/js/populate.js  
ENTRYPOINT forever /home/root/js/server.js

