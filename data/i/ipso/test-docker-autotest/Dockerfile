FROM alpine:latest  
RUN set -ex && mkdir -p /app && apk update && apk add bash && apk add mysql-
client  
WORKDIR /app  
COPY . /app  
CMD ls -lart /var/log  

