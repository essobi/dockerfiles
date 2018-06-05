FROM tomcat:8.0.37-jre8  
MAINTAINER "Naveen-DBSync <naveen.p@mydbsync.com>"  
RUN mkdir -p /usr/local/tomcat/CloudWF  
COPY server/CloudWF /usr/local/tomcat/CloudWF  
RUN mkdir -p /usr/local/tomcat/scripts  
COPY server/scripts /usr/local/tomcat/scripts  
RUN mkdir -p /usr/local/tomcat/work  
COPY server/work /usr/local/tomcat/work  
ADD server/conf/Catalina/localhost/DBSync.xml
/usr/local/tomcat/conf/Catalina/localhost/  

