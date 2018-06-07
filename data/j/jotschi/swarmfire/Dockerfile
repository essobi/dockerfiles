FROM java:openjdk-8-jre  
MAINTAINER Johannes Schüth <docker@jotschi.de>  
  
ARG BASEDIR  
ENV DATA EMPTY  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

