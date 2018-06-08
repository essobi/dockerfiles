FROM node:7  
MAINTAINER Konpat Preechakul <the.akita.ta@gmail.com>  
  
RUN npm install -g mocha source-map-support  
  
WORKDIR /workdir  
  
ENTRYPOINT ["mocha --no-timeouts --requires=source-map-support/register"]  

