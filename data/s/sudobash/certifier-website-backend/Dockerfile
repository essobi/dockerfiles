FROM alpine:3.7  
WORKDIR /certifier  
ADD ./ /certifier  
RUN apk upgrade  
RUN apk add \--update --no-cache make gcc g++ python nodejs git && \  
npm install --prefix /certifier/backend && \  
apk del make gcc g++ python  

