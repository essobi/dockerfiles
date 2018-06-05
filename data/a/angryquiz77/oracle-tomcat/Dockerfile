FROM ubuntu:14.04  
#https://github.com/cmoro-deusto/docker-tomcat8  
MAINTAINER AngryQuiz <support@angryquiz.com>  
  
# Set locales  
RUN locale-gen en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
ENV LC_CTYPE en_GB.UTF-8  
# Fix sh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install dependencies  
RUN apt-get update  
RUN apt-get install -y git build-essential curl wget software-properties-
common  
  
#Install utils  
RUN apt-get install -y openssh-server  
RUN apt-get install -y nano  
  
#Prepare redis  
RUN apt-get install -y redis-server  
  
RUN mkdir /dist  
ADD dist /dist  
  
#Install JDK  
RUN set -x \  
\  
&& cd /dist \  
&& tar -xzvf jdk-8u131-linux-x64.tar.gz \  
&& rm -rf jdk-8u131-linux-x64.tar.gz  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /dist/jdk1.8.0_131  
  
RUN set -x \  
\  
&& cd /dist \  
&& tar -xzvf apache-maven-3.5.0-bin.tar.gz \  
&& rm -rf apache-maven-3.5.0-bin.tar.gz  
  
ENV PATH $PATH:/dist/apache-maven-3.5.0/bin:$JAVA_HOME/bin  
  
ENV M2_HOME /dist/apache-maven-3.5.0/bin  
  
# Get Tomcat  
RUN cd /dist && tar -xzvf apache-tomcat-8.5.8.tar.gz \  
&& mv /dist/apache-tomcat-8.5.8 /opt/tomcat  
  
RUN cd /dist && rm -rf apache-tomcat-8.5.8.tar.gz  
  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
# Add admin/admin user  
ADD tomcat-users.xml /opt/tomcat/conf/  
  

