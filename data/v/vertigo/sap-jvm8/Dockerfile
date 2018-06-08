# Base CentOS 7 with SAP tools  
#  
# . SAP JVM  
#  
# Tools downloaded from https://tools.hana.ondemand.com/#cloud  
#  
FROM vertigo/docker-base:latest  
  
MAINTAINER Rubens Neto <rubens@vertigo.com.br>  
  
ADD src/download-tools.sh /opt/  
  
RUN sh /opt/download-tools.sh && \  
yum localinstall /opt/sap-jvm.rpm -y && \  
rm /opt/sap-jvm.rpm && \  
mkdir /opt/cloud-sdk && \  
unzip /opt/cloud-sdk.zip -d /opt/cloud-sdk/ && \  
mkdir /opt/sapcc && \  
tar -xzf /opt/sapcc.tar.gz -C /opt/sapcc/ && \  
rm /opt/cloud-sdk.zip && \  
rm /opt/sapcc.tar.gz  
ENV JAVA_HOME /usr/java/sapjvm_8_latest  
RUN alternatives --install /usr/bin/java java
/usr/java/sapjvm_8_latest/bin/java 1

