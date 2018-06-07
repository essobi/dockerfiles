FROM node:8.0-alpine  
  
RUN apk update && apk add ca-certificates wget && update-ca-certificates  
  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
RUN chmod +x /usr/local/bin/dumb-init  
  
WORKDIR /opt/docker-intro  
COPY package.json /opt/docker-intro  
RUN apk --no-cache add --virtual native-deps \  
g++ gcc libgcc libstdc++ linux-headers make python && \  
npm install --quiet node-gyp -g &&\  
npm install --quiet && \  
apk del native-deps  
COPY . /opt/docker-intro  
  
EXPOSE 8000  
CMD ["/usr/local/bin/dumb-init", "npm", "start"]  

