FROM alpine:edge  
  
RUN set -ex; \  
adduser -D codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories; \  
# Installs Racket 6.12 as of 2018-04-08  
apk --no-cache add racket@testing;  
  
WORKDIR /workspace  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  

