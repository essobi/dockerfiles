FROM gliderlabs/alpine:latest  
  
MAINTAINER TSUYOSHI TORII toritori0318  
  
RUN apk update && \  
apk add curl git openssh-client ca-certificates nodejs \  
bash wget tar gzip rsync py-pip make g++ && \  
rm /var/cache/apk/*  
  
# node cli  
RUN npm install -g grunt-cli gulp  

