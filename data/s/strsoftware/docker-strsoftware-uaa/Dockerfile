FROM java:openjdk-8u66-jre  
MAINTAINER STR Software  
  
ENV UAA_CONFIG_PATH /uaa  
ENV CATALINA_HOME /tomcat  
  
ADD run.sh /tmp/  
ADD uaa.yml /uaa/uaa.yml  
RUN chmod +x /tmp/run.sh  
  
RUN wget -q
https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.0.M9/bin/apache-
tomcat-9.0.0.M9.tar.gz  
RUN wget -qO-
https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.0.M9/bin/apache-
tomcat-9.0.0.M9.tar.gz.md5 | md5sum -c -  
  
RUN tar zxf apache-tomcat-9.0.0.M9.tar.gz  
RUN rm apache-tomcat-9.0.0.M9.tar.gz  
  
RUN mkdir /tomcat  
RUN mv apache-tomcat-9.0.0.M9/* /tomcat  
RUN rm -rf /tomcat/webapps/*  
  
ADD cloudfoundry-identity-uaa-3.6.0.war /tomcat/webapps/  
RUN mv /tomcat/webapps/cloudfoundry-identity-uaa-3.6.0.war
/tomcat/webapps/ROOT.war  
  
#VOLUME ["/uaa"]  
EXPOSE 8080  
CMD ["/tmp/run.sh"]  

