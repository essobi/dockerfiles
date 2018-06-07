FROM docker:latest  
  
MAINTAINER Caspar <caspar_wei@itri.org.tw>  
  
RUN apk --no-cache update && apk --no-cache add python py-pip py-setuptools
ca-certificates groff less && pip --no-cache-dir install awscli && rm -rf
/var/cache/apk/*  

