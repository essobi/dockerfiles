############################################################  
# Dockerfile to build minicom container images  
# Based on Alpine linux  
############################################################  
  
# Set the base image to alpine  
FROM alpine  
  
# File Author / Maintainer  
MAINTAINER yoni davidson  
  
# Update the repository sources list  
RUN apk update && \  
apk add minicom && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
ENV device=/dev/mydevice  
ENV baud=115200  
  
CMD minicom -D $device -b $baud  

