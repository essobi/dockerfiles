FROM alpine  
MAINTAINER icecubetray  
CMD sh  
  
# Install packages.  
RUN apk update; \  
apk \  
add -t icy-dev \  
gcc make \  
libc-dev \  
git dos2unix; \  
rm -Rf \  
/var/cache/apk/* \  
/tmp/*;  
  
# Ensure /repositories exists.  
RUN mkdir -p /repositories;  
  
# Install info script.  
COPY sbin/alpine-icy-info.sh /usr/sbin/alpine-icy-info  
RUN dos2unix -u /usr/sbin/alpine-icy-info;  

