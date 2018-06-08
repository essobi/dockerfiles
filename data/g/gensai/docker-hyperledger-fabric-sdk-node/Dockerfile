FROM node:6.9.1-alpine  
  
RUN apk add --update --no-cache \  
alpine-sdk \  
python \  
py-pip \  
libc6-compat  
  
WORKDIR /home/node  
USER node  
  
RUN git clone -b \  
v1.0.0-alpha.1 \  
https://github.com/hyperledger/fabric-sdk-node.git  
  
WORKDIR fabric-sdk-node  
  
RUN npm install  
RUN ./node_modules/.bin/gulp ca  
RUN ./node_modules/.bin/gulp doc  

