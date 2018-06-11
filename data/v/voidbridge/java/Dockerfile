FROM voidbridge/centos7  
MAINTAINER Voidbridge <developers@voidbridge.com>  
ENV JDK_VERSION=1.8.0_91  
  
LABEL io.k8s.description="Java base image" \  
io.k8s.display-name="Java" \  
io.openshift.tags="java"  
  
COPY ./jdk-8u91-linux-x64.rpm /tmp  
RUN rpm -ivh /tmp/jdk-8u91-linux-x64.rpm && \  
rm /tmp/jdk-8u91-linux-x64.rpm  

