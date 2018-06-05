FROM alpine:latest  
  
RUN \  
apk update && \  
apk upgrade && \  
rm -rf /var/cache/apk/*  
  
ONBUILD RUN apk update && apk upgrade  

