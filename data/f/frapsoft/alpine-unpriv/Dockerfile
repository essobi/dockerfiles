FROM alpine:edge  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
RUN mkdir /app && \  
adduser -h /app -s /sbin/nologin -D app && \  
chown app:app /app  
  
USER app  
  
ENV HOME=/app  
  
WORKDIR $HOME  

