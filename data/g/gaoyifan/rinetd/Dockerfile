FROM smartentry/alpine:3.4-0.3.8  
MAINTAINER Yifan Gao <docker@yfgao.com>  
  
ADD . $ASSETS_DIR  
  
RUN smartentry.sh build  
  
VOLUME /var/log  
  
CMD ["rinetd", "-f", "-c", "/etc/rinetd/rinetd.conf"]  

