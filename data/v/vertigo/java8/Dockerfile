# Base Java Image  
FROM vertigo/docker-base:latest  
  
MAINTAINER Rubens Neto  
  
WORKDIR /opt  
ARG LOCALJDK  
  
ADD src/downloadJDK.sh /opt/downloadJDK.sh  
RUN sh /opt/downloadJDK.sh && \  
yum localinstall /opt/jdk.rpm -y && \  
rm /opt/jdk.rpm && \  
yum clean all  
  
#ENV JAVA_HOME /usr/lib/jvm/java  
#RUN echo "JAVA_HOME=/usr/lib/jvm/java" >> /etc/environment  

