FROM mirkosertic/basejava7  
MAINTAINER Mirko Sertic <mirko.sertic@web.de>  
  
# Install Apache Tomcat  
RUN mkdir /opt/Tomcat6 && \  
cd /opt/Tomcat6 && \  
wget "http://ftp.halifax.rwth-
aachen.de/apache/tomcat/tomcat-6/v6.0.41/bin/apache-tomcat-6.0.41.tar.gz" && \  
tar xfz apache-tomcat-6.0.41.tar.gz && \  
ln -s /opt/Tomcat6/apache-tomcat-6.0.41 /opt/Tomcat6/current_tomcat && \  
rm /opt/Tomcat6/apache-tomcat-6.0.41.tar.gz  
  
COPY tomcat-start.sh /opt/Tomcat6/tomcat-start.sh  
  
RUN chmod -R 755 /opt/Tomcat6  
  
# Finally run it  
EXPOSE 8080  
ENTRYPOINT ["/opt/Tomcat6/tomcat-start.sh"]  
  

