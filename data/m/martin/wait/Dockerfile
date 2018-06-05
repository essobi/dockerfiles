FROM alpine:3.7  
MAINTAINER Martin van Beurden <chadoe@gmail.com>  
  
RUN apk add --no-cache netcat-openbsd  
  
ADD wait /wait  
  
ENTRYPOINT ["/wait"]  

