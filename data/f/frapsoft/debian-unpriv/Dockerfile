FROM debian:jessie-slim  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
RUN mkdir /app && \  
adduser --gecos "" \--disabled-login --home /app \--no-create-home --shell
/bin/false app && \  
chown app:app /app  
  
USER app  
  
ENV HOME=/app  
  
WORKDIR $HOME  

