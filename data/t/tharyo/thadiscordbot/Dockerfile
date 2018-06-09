FROM node:alpine  
  
ENV TZ Europe/Vienna  
RUN apk add --update tzdata \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /app  
COPY "./package.json" "./package.json"  
RUN npm install --production \  
&& npm cache clean  
  
COPY "./lib" "./lib/"  
ENTRYPOINT node "./lib/index.js"

