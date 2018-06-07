FROM indigolabs/base:java8  
MAINTAINER Nicolas Seigneur <nseigneur@indigoconsulting.ca>  
  
#Download Tomcat 8.0.37  
RUN wget --quiet
https://archive.apache.org/dist/tomcat/tomcat-8/v8.0.37/bin/apache-
tomcat-8.0.37.zip && unzip apache-tomcat-8.0.37.zip && mv ./apache-
tomcat-8.0.37 /opt/tomcat/ && rm -f ./apache-tomcat-8.0.37.zip  
  
#Copy Basic Start and tail Script  
COPY ./tomcatstart /etc/init.d/tomcatstart  
  
#Make required scripts executable  
RUN chmod +x /opt/tomcat/bin/startup.sh && chmod +x
/opt/tomcat/bin/shutdown.sh && chmod +x /opt/tomcat/bin/catalina.sh  
RUN chmod 744 /etc/init.d/tomcatstart  
  
#Expose the tomcat well-known connector ports  
EXPOSE 8080 8443

