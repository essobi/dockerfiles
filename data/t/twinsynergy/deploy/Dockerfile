FROM alpine:3.6  
MAINTAINER Arnon kijlerdphon <snappy.kop@gmail.com>  
  
RUN packages=' \  
openssh \  
sshpass \  
openssl \  
' \  
set -x \  
&& apk --update add $packages \  
&& rm -rf /var/cache/apk/*  
  

