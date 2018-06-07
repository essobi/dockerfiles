FROM izonder/anny:latest  
  
MAINTAINER Dmitry Morgachev <izonder@gmail.com>  
  
ENV OPENJDK_VERSION=8-jre  
  
RUN set -x \  
  
##############################################################################  
# Install dependencies  
##############################################################################  
  
&& apk add --no-cache \  
openjdk${OPENJDK_VERSION}  
  
ENTRYPOINT ["/init"]  

