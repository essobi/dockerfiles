FROM xataz/node:4.2-onbuild  
RUN apk --update add bash wget unzip ca-certificates && \  
wget https://ghost.org/zip/ghost-latest.zip && unzip ghost-latest.zip -d
/ghost && \  
rm -f ghost-latest.zip && \  
apk del wget unzip && rm -rf /var/cache/apk/* && \  
cd /ghost && \  
npm install --production && \  
sed 's/127.0.0.1/0.0.0.0/' config.example.js > config.js  
  
ADD start /start  
  
ENV NODE_ENV production  
  
VOLUME ["/ghost-override"]  
  
WORKDIR /ghost  
  
CMD ["bash","/start"]  
  
EXPOSE 2368  

