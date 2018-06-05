FROM debian:wheezy  
MAINTAINER finalcut bill@rawlinson.us  
  
ENV REFRESHED_AT 2014_08_19_1  
  
ADD https://github.com/framework-one/fw1/archive/v3.0-beta1.tar.gz
/tmp/fw1.tar.gz  
  
WORKDIR /tmp  
  
RUN tar -xzf fw1.tar.gz  
RUN mv fw1-3.0-beta1 fw1  
RUN rm fw1.tar.gz  
  
VOLUME /tmp/fw1  
  
CMD ["/bin/sh"]  

