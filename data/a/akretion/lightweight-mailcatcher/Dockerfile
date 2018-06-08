FROM ubuntu-debootstrap:14.04  
MAINTAINER AKRETION <sebastien.beau@akretion.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD install.sh install.sh  
  
RUN sh install.sh  
  
EXPOSE 1080  
EXPOSE 1025  
ENTRYPOINT ["mailcatcher", "--smtp-ip=0.0.0.0", "--http-ip=0.0.0.0", "--
foreground"]  

