FROM debian:jessie  
MAINTAINER lfelipedeoliveira, felipe@lfelipedeoliveira.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y; \  
apt-get install -y openjdk-7-jre-headless file; \  
apt-get clean  
  
ADD
http://downloads.sourceforge.net/project/ngopt/a5_miseq_linux_20141120.tar.gz
/tmp/a5_miseq.tar.gz  
  
RUN mkdir /a5_miseq; \  
tar xzf /tmp/a5_miseq.tar.gz --directory /a5_miseq --strip-components=1; \  
rm /tmp/a5_miseq.tar.gz  

