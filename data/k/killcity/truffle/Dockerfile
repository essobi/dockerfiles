FROM node:8.6-alpine  
  
RUN mkdir /truffle  
RUN chown node /truffle  
WORKDIR /truffle  
  
RUN apk add -t .gyp --no-cache git python g++ make \  
&& npm install -g truffle@3.4.11 \  
&& npm install -g ethereumjs-testrpc  

