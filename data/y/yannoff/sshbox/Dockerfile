# vim: ft=Dockerfile  
#  
# @package sshbox  
# @author yannoff <https://github.com/yannoff>  
# @license MIT  
#  
FROM yannoff/alpine  
  
MAINTAINER Yannoff <https://github.com/yannoff>  
  
RUN \  
apk add --no-cache --update \  
openssh-client \  
su-exec \  
curl \  
git \  
; \  
mkdir -p /app/src; \  
mkdir -p /app/ssh; \  
rm -rfv /var/cache/apk; \  
rm -rfv /usr/share/apk/keys;  
  
COPY entrypoint.sh /usr/bin  
VOLUME [ "/app/ssh" ]  
ENTRYPOINT [ "entrypoint.sh" ]  

