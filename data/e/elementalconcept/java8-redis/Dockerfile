# Use ubuntu 16 based java 8 image  
FROM cogniteev/oracle-java:java8  
MAINTAINER laszlo@elementalconcept.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update apt-get  
RUN apt-get -qq update  
  
# install redis  
RUN apt-get install -y redis-server  
  
RUN mkdir /app  
WORKDIR /app  
  
CMD /bin/bash  

