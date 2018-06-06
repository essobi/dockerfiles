FROM alpine:latest  
  
LABEL maintainer="David Clutter <cluttered.code@gmail.com>"  
  
ENV RETHINKDB_PASSWORD admin  
  
RUN apk --no-cache update &&\  
apk --no-cache upgrade &&\  
apk --no-cache add rethinkdb &&\  
mkdir -p /data/rethinkdb  
  
WORKDIR /data/rethinkdb  
VOLUME /data/rethinkdb  
  
#Ports: process cluster webui  
EXPOSE 28015 29015 8080  
ENTRYPOINT rethinkdb --directory /data/rethinkdb --initial-password
${RETHINKDB_PASSWORD} \--bind all

