FROM centos  
  
MAINTAINER <contato@eduardomedeiros.me>  
  
# Expose the ports  
EXPOSE 8080  
# Set the TOMCAT_VERSION env variable  
ENV TOMCAT_RELEASE 8.5.29  
ENV TOMCAT_VERSION 8  
# Add user and group wildfly  
RUN groupadd apache  
RUN adduser -g apache tomcat  
  
# Install OpenJDK 8  
RUN yum install java-1.8.0-openjdk-devel -y  
  
# Download and install tomcat  
RUN curl -O
http://mirror.nbtelecom.com.br/apache/tomcat/tomcat-$TOMCAT_VERSION/v$TOMCAT_RELEASE/bin/apache-
tomcat-$TOMCAT_RELEASE.tar.gz  
RUN tar xzvf apache-tomcat-$TOMCAT_RELEASE.tar.gz -C /opt  
RUN ln -s /opt/apache-tomcat-$TOMCAT_RELEASE /opt/tomcat  
  
# Add user tomcat / pass: tomcat  
ADD tomcat-users.xml /opt/tomcat/conf/  
RUN chown -R tomcat:apache /opt/apache-tomcat-$TOMCAT_RELEASE  
  
# Deploy  
USER tomcat  
ADD hello.war /opt/tomcat/webapps/  
  
# Set the default command to run on boot  
# This will boot TOMCAT  
USER tomcat  
CMD ["/opt/tomcat/bin/catalina.sh", "run"]  

