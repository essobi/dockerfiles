FROM node:8-alpine  
  
RUN apk update && \  
apk --no-cache add openssl && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-2.25-r0.apk && \  
apk --no-cache add glibc-2.25-r0.apk && \  
rm -f glibc-2.25-r0.apk  

