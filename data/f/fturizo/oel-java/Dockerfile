# We start using Oracle Linux official image repository  
FROM oraclelinux  
  
MAINTAINER Fabio Turizo <fabio.turizo@gmail.com>  
  
WORKDIR /opt/installers/  
  
ENV JDK_URL http://download.oracle.com/otn-
pub/java/jdk/7u75-b13/jdk-7u75-linux-x64.rpm  
  
RUN yum install wget -y && \  
wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" ${JDK_URL} && \  
rpm -Uvh jdk-7u75-linux-x64.rpm && \  
alternatives --install /usr/bin/java java /usr/java/latest/jre/bin/java 200000
&& \  
alternatives --install /usr/bin/javaws javaws /usr/java/latest/jre/bin/javaws
200000 && \  
rm -rdf /opt/installers && \  
yum remove wget -y  

