FROM mirkosertic/basejava8  
MAINTAINER Mirko Sertic <mirko.sertic@web.de>  
  
# Install Apache Tomcat  
RUN mkdir /opt/Tomcat8 && \  
cd /opt/Tomcat8 && \  
wget
"http://mirror.serversupportforum.de/apache/tomcat/tomcat-8/v8.0.12/bin/apache-
tomcat-8.0.12.tar.gz" && \  
tar xfz apache-tomcat-8.0.12.tar.gz && \  
ln -s /opt/Tomcat8/current_tomcat /opt/Tomcat8/apache-tomcat-8.0.12 && \  
rm /opt/Tomcat8/apache-tomcat-8.0.12.tar.gz  
  
COPY tomcat-start.sh /opt/Tomcat8/tomcat-start.sh  
  
RUN chmod -R 755 /opt/Tomcat8  
  
# Finally run it  
EXPOSE 8080  
ENTRYPOINT ["/opt/Tomcat8/tomcat-start.sh"]  
  

