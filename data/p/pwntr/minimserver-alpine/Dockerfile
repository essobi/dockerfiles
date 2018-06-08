FROM alpine:latest  
MAINTAINER Peter Winter <peter@pwntr.com>  
LABEL Description="Simple and lightweight MinimServer Docker container, based
on Alpine Linux." Version="0.1"  
  
# update the base system  
RUN apk update && apk upgrade  
  
# install Java 8  
RUN apk add openjdk8-jre  
  
# add a non-root user and group called "minim" with no password, no home dir,
no shell, and gid/uid set to 1000  
RUN addgroup -g 1000 minim && adduser -H -D -G minim -s /bin/false -u 1000
minim  
  
# download and extract MinimServer  
RUN wget -O minimserver.tar.gz
http://jminim.com/abra/MinimServer-0.8.3f-linux-x64.tar.gz && \  
tar -xvzf minimserver.tar.gz && \  
rm minimserver.tar.gz  
  
# HTTP (data) and UPnP (discovery) ports used by MinimServer  
EXPOSE 9790 9791  
VOLUME /music  
  
USER minim  
  
ENTRYPOINT ["/minimserver/minimserver-0.8.3f/bin/startc"]  

