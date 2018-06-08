FROM centos:latest  
  
MAINTAINER Andrus Adamchik <andrus at objectstyle dot com>  
  
LABEL name=objectstyle-java8  
  
RUN yum -y install java-1.8.0-openjdk-devel  
RUN yum -y update; yum clean all  
  
ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk  
ENV PATH=${JAVA_HOME}/bin:${PATH}  
  

