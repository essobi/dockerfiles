FROM tomcat  
MAINTAINER Vitradisa Pratama (vitradisapratama@gmail.com)  
  
RUN wget
http://nchc.dl.sourceforge.net/project/geoserver/GeoServer/2.7.2/geoserver-2.7.2-war.zip
-P /usr/local/tomcat/webapps/  
  
RUN unzip -o /usr/local/tomcat/webapps/geoserver-2.7.2-war.zip -d
/usr/local/tomcat/webapps/  
  
RUN rm /usr/local/tomcat/webapps/geoserver-2.7.2-war.zip  
  
ENV CATALINA_BASE = /usr/local/tomcat  
ENV CATALINA_HOME = /usr/local/tomcat  
ENV CATALINA_TMPDIR = /usr/local/tomcat/temp  
ENV JRE_HOME = /usr  
ENV CLASSPATH =
/usr/local/tomcat/bin/bootstrap.jar:/usr/local/tomcat/bin/tomcat-juli.jar  
  
EXPOSE 8080

