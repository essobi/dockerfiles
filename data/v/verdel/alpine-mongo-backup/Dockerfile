FROM mongo:latest  
MAINTAINER Vadim Aleksandrov <valeksandrov@me.com>  
  
COPY rootfs /  
  
RUN chmod 755 /sbin/*.sh  
  
VOLUME ["/backup"]  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]

