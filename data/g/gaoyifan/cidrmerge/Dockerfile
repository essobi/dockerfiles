FROM smartentry/alpine:3.5-0.3.13  
MAINTAINER Yifan Gao <docker@yfgao.com>  
  
ADD .docker $ASSETS_DIR  
  
RUN smartentry.sh build  
  
ENTRYPOINT ["/usr/bin/cidrmerge"]  
  
CMD []  

