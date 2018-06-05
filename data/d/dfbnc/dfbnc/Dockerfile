FROM ubuntu:xenial  
MAINTAINER Shane Mc Cormack <dataforce@dataforce.org.uk>  
  
RUN \  
apt-get update && \  
apt-get -y install \  
curl \  
openjdk-8-jre-headless  
  
RUN curl -L -o /DFBnc.jar
https://github.com/ShaneMcC/DFBnc/releases/download/0.4.1/dfbnc.jar  
  
EXPOSE 33262 33263  
VOLUME ["/var/lib/dfbnc"]  
  
WORKDIR /var/lib/dfbnc  
  
CMD ["/usr/bin/java", "-jar", "/DFBnc.jar", "--config", "/var/lib/dfbnc", "--
foreground"]  

