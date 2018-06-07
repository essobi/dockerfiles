FROM tomcat:7.0.70-jre7  
  
MAINTAINER Mariusz Wyszomierski <mariusz@wyszomierski.pl>  
  
ENV KUNAGI_VERSION 0.26.2  
ENV KUNAGI_SHA1 159276bad2823c09e66d3588f3720179875fea90  
  
RUN curl -o /usr/local/tomcat/webapps/kunagi.war -SL
http://kunagi.org/releases/${KUNAGI_VERSION}/kunagi.war \  
&& echo "$KUNAGI_SHA1 /usr/local/tomcat/webapps/kunagi.war" | sha1sum -c -  

