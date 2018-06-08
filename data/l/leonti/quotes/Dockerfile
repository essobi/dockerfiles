FROM leonti/tomcat  
MAINTAINER Leonti Bielski "leonti.bielski@gmail.com"  
RUN echo "deb http://archive.ubuntu.com/ubuntu saucy main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y install openjdk-7-jre-headless  
RUN apt-get -y install tomcat7  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64" >> /etc/default/tomcat7

