FROM alpine:3.6  
  
RUN set -ex; \  
adduser -D codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN apk add \--no-cache perl;  
  
WORKDIR /workspace  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  

