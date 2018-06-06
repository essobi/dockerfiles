FROM node:8-alpine  
  
RUN apk add --no-cache make python openssl  
  
RUN wget
https://github.com/ZencashOfficial/secnodetracker/archive/v0.2.1-beta.tar.gz \  
&& tar -xvf v0.2.1-beta.tar.gz \  
&& rm -rf v0.2.1-beta.tar.gz \  
&& mv secnodetracker-0.2.1-beta app  
  
WORKDIR /app  
RUN npm install && npm cache clean --force  
  
CMD ["node", "app"]  

