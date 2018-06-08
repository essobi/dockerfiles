FROM alpine:3.6  
  
RUN set -ex; \  
adduser -D codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
apk add \--no-cache lua5.2 lua5.2-busted; \  
ln -s /usr/bin/lua5.2 /usr/bin/lua; \  
ln -s /usr/bin/busted-5.2 /usr/bin/busted;  
  
WORKDIR /workspace  
  
COPY rootfs/runner /runner  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  

