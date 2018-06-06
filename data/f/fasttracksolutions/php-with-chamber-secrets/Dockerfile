FROM php:alpine  
  
RUN apk update && apk upgrade && \  
apk add --no-cache openssl ca-certificates  
  
RUN wget
https://github.com/segmentio/chamber/releases/download/v1.5.0/chamber-v1.5.0-linux-
amd64 -O /bin/chamber && \  
chmod +x /bin/chamber

