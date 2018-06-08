# 2016-03-08  
# Tomcat container for Quartermaster backup  
FROM tomcat:7.0.68-jre8  
MAINTAINER aaryndo@gmail.com  
  
ADD server.xml /usr/local/tomcat/conf/server.xml  
ADD web.xml /usr/local/tomcat/conf/web.xml  
  
RUN ln -sf /usr/share/zoneinfo/Europe/Warsaw /etc/localtime  
RUN keytool -genkey -alias tomcat -keyalg RSA -keystore
/usr/local/tomcat/conf/tomcat.keystore -storepass SheIsNotPerfectButSheTries
-dname CN=Aari,OU=Quartermaster,O=Aari,L=KR,ST=K,C=PL -keypass
SheIsNotPerfectButSheTries  
  
CMD rm -rf /usr/local/tomcat/webapps/* && cp -f /webapps/quartermaster.war
/usr/local/tomcat/webapps/ && catalina.sh start && tail -f /dev/null  
  

