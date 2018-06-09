FROM alpine:3.4  
MAINTAINER Emory Merryman emory.merryman@gmail.com  
RUN \  
apk update && \  
apk upgrade && \  
apk add docker && \  
apk add sudo && \  
adduser -D user && \  
mkdir /usr/local/src && \  
chown user:user /usr/local/src && \  
mkdir /usr/local/sbin && \  
true  
VOLUME ["/usr/local/src"]  
WORKDIR /usr/local/src  

