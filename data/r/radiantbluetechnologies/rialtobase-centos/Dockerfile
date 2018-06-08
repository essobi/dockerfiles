# radiantbluetechnologies/rialtobase-centos  
# centos7, plus some common stuff we use everywhere  
FROM centos:centos7  
MAINTAINER mpg@flaxen.com  
  
# Install prepare infrastructure  
RUN true \  
&& yum -y update \  
&& yum -y install wget curl unzip tar \  
&& yum -y install epel-release \  
&& yum clean all  

