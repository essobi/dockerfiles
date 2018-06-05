FROM alpine:latest  
RUN set -ex && mkdir -p /app && apk update && apk add bash  
WORKDIR /app  
COPY docker-cloud-test.sh /app  
CMD ls -lart /var/log  

