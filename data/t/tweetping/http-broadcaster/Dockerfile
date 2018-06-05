FROM node:argon  
  
MAINTAINER Franck Ernewein <franck.ernewein@tweetping.net>  
  
COPY package.json /src/package.json  
WORKDIR /src  
RUN npm install --production  
  
COPY entrypoint.sh /src/entrypoint.sh  
COPY bin.js /src/bin.js  
COPY lib/createServer.js /src/lib/createServer.js  
  
EXPOSE 3000  
ENTRYPOINT ["/src/entrypoint.sh"]  

