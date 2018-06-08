FROM lorislab/base:latest  
  
MAINTAINER Andrej Petras, andrej@lorislab.org  
  
RUN yum -y install java-1.8.0-openjdk-devel && yum clean all  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0  
  
ENV PATH "$PATH":/${JAVA_HOME}/bin:.:  

