FROM alpine:3.7  
RUN apk update &&\  
apk add --no-cache \  
openssl &&\  
mkdir -p /ssl  
  
VOLUME /ssl  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT "/entrypoint.sh"  

