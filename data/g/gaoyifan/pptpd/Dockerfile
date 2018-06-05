FROM smartentry/centos:7-0.3.8  
MAINTAINER Yifan Gao <docker@yfgao.com>  
  
ADD . $ASSETS_DIR  
  
RUN smartentry.sh build  
  
CMD ["/usr/sbin/pptpd", "-f"]  

