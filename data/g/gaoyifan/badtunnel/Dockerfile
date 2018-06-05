FROM smartentry/alpine:3.4-0.3.2  
MAINTAINER Yifan Gao <docker@yfgao.com>  
  
ADD . $ASSETS_DIR  
  
RUN /sbin/smartentry.sh build  
  
VOLUME /var/log  
  
CMD ["/usr/bin/supervisord"]  

