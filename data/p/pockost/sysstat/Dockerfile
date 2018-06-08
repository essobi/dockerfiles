FROM alpine  
MAINTAINER Romain THERRAT <romain@pockost.com>  
  
# most utilities are from the latest stable alpine release  
# add some additional utilities that are only available in 'testing'  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add --update sysstat && \  
rm -rf /var/cache/apk/*  
  

