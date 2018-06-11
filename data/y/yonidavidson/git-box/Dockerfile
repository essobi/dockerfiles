############################################################  
# Dockerfile to build vim container images  
# Based on Alpine linux  
############################################################  
  
# Set the base image to alpine  
FROM alpine  
  
# File Author / Maintainer  
MAINTAINER yoni davidson  
  
# Update the repository sources list  
RUN apk --update add git && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
ADD ./addons/.gitconfig /root/  
  
ENTRYPOINT /bin/sh  

