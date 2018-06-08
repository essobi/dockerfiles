# ubuntu base image  
FROM ubuntu:14.04  
MAINTAINER <Author name and email address>  
  
RUN apt-get update  
  
RUN mkdir -p /version; \  
/usr/bin/lsb_release -a > /version/base-image-build-"$(/usr/bin/lsb_release
-si):$(/usr/bin/lsb_release -sr)-$(date -u +"%Y-%m-%d-%H:%M:%S-UTC")"  
  
CMD /bin/bash  

