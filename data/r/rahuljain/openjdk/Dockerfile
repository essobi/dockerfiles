###############################################################################################  
# Docker container image that consists of an Alpine base image with Open JDK
installed.  
#  
# Run: READ.md  
###############################################################################################  
  
FROM rahuljain/base:1.0.0  
  
LABEL maintainer="rahuljain"  
  
ENV VERSION 1.8.0_161-b12  
ENV JAVA_VERSION=8 JAVA_UPDATE=161 JAVA_BUILD=12  
ENV JAVA_HOME=/usr PATH=/usr/bin:$PATH  
  
# installing openjdk  
RUN apk add --no-cache
openjdk8=${JAVA_VERSION}.${JAVA_UPDATE}.${JAVA_BUILD}-r0 --update-cache
--repository http://dl-3.alpinelinux.org/alpine/edge/community --allow-
untrusted  

