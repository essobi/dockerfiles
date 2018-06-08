FROM debian:jessie  
  
MAINTAINER Matthias Grüter <matthias@grueter.name>  
  
# disable debconf frontend warnings  
ENV DEBIAN_FRONTEND noninteractive  
  
# install java  
RUN apt-get update && \  
apt-get install -y openjdk-7-jre-headless && \  
apt-get clean  
  
CMD ["java", "-version"]  

