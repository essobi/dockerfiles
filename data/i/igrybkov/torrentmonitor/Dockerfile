#------------------------------------------------------------------------------  
# Set the base image for subsequent instructions:  
#------------------------------------------------------------------------------  
FROM nawa/torrentmonitor:latest  
  
#------------------------------------------------------------------------------  
# Install:  
#------------------------------------------------------------------------------  
  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
RUN apk update \  
&& apk upgrade \  
&& apk add --upgrade py2-asn1-modules zlib libc-utils py2-pip deluge@testing \  
\--no-cache --repository http://nl.alpinelinux.org/alpine/edge/main \  
&& apk add --no-cache py2-service_identity --repository
http://nl.alpinelinux.org/alpine/edge/community \  
&& (apk del --purge deps; rm -rf /tmp/* /var/cache/apk/*)  

