# ubuntu base image  
FROM ubuntu:14.04  
  
MAINTAINER <Author name and email address>  
  
# resynchronize the package index files  
# packages no longer required are removed  
# install the newest versions of all packages currently installed  
RUN apt-get -qy update && apt-get -qy autoremove && apt-get -qy dist-upgrade  
  
# Create a time and date stamp of this build in /version  
RUN mkdir -p /version; \  
/usr/bin/lsb_release -a > /version/base-image-"$(/usr/bin/lsb_release
-si):$(/usr/bin/lsb_release -sr)-$(date -u +"%Y-%m-%d-%H:%M:%S-UTC")"  
  
CMD /bin/bash  

