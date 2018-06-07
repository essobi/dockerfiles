FROM openjdk:7-alpine  
  
add . /app  
  
RUN mkdir /opt && \  
cd /opt && \  
apk add \--no-cache ca-certificates wget && \  
wget http://www-eu.apache.org/dist/maven/maven-3/3.0.5/binaries/apache-
maven-3.0.5-bin.zip && \  
unzip apache-maven-3.0.5-bin.zip && \  
wget https://archive.apache.org/dist/tomcat/tomcat-6/v6.0.0/bin/apache-
tomcat-6.0.0.zip && \  
unzip apache-tomcat-6.0.0.zip && \  
rm *.zip && \  
chmod +x /opt/apache-tomcat-6.0.0/bin/*.sh && \  
rm /opt/apache-tomcat-6.0.0/webapps/* -rf && \  
  
cd /app && \  
/opt/apache-maven-3.0.5/bin/mvn package && \  
mv target/struts-networkpolicy-demo*.war /opt/apache-
tomcat-6.0.0/webapps/ROOT.war && \  
chmod 777 /opt/apache-tomcat-6.0.0 -R && \  
  
rm ~/.m2 -rf && \  
rm /opt/apache-maven* -rf  
  
  
EXPOSE 8080  
  
CMD /opt/apache-tomcat-6.0.0/bin/catalina.sh run  

