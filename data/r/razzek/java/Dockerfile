FROM openjdk:8-jdk-alpine  
  
ARG user=appuser  
ARG group=appuser  
ARG uid=30000  
ARG gid=30000  
  
RUN apk add \--no-cache \  
tini \  
&& addgroup ${group} -g ${gid} \  
&& adduser -u ${uid} -G ${group} -s /sbin/nologin -D ${user}  

