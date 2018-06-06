FROM gliderlabs/alpine:3.2  
  
RUN apk --update add curl && \  
rm -rf /var/apk/cache/* && \  
curl -L https://github.com/sequenceiq/docker-alpine-
dig/releases/download/v9.10.2/dig.tgz|tar -xzv -C /usr/local/bin/  

