FROM ubuntu:16.04  
MAINTAINER M Parker <mparker17@536298.no-reply.drupal.org>  
  
RUN apt-get -y update && \  
apt-get -y install android-tools-fastboot  
  
VOLUME [ "/dev/bus/usb", "/fastboot" ]  
WORKDIR /fastboot  
  
# Run fastboot by default, with "help" as the default argument. This can be  
# overridden at `docker run`-time. See README for more information.  
ENTRYPOINT [ "fastboot" ]  
CMD [ "help" ]  

