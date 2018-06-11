FROM ubuntu:14.04.4  
MAINTAINER zopanix <zopanix@gmail.com>  
  
ENV CASPERJS_VERSION=1.1.3  
ADD ./resources /resources  
  
RUN /resources/build && rm -rf resources  
  
ENTRYPOINT ["casperjs"]  
  
VOLUME /data  
  
WORKDIR /data  

