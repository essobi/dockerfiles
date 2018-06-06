FROM apsl/java:7  
# parents: apsl/circusbase > apsl/java6  
MAINTAINER APSL bcabezas@apsl.net  
  
ENV TOMCAT_MAJOR_VERSION 7  
ENV TOMCAT_MINOR_VERSION 7.0.55  
ENV CATALINA_HOME /opt/tomcat  
  
  
# INSTALL TOMCAT  
ADD
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz /  
RUN \  
tar zxf apache-tomcat-*.tar.gz && \  
rm apache-tomcat-*.tar.gz && \  
mv apache-tomcat* /opt/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin  
VOLUME ["/opt/tomcat/logs", "/opt/tomcat/work", "/opt/tomcat/temp",
"/tmp/hsperfdata_root" ]  
  
# Remove unneeded apps  
RUN \  
rm -rf /opt/tomcat/webapps/host-manager ; \  
rm -rf /opt/tomcat/webapps/examples ;\  
rm -rf /opt/tomcat/webapps/docs/ ;\  
rm -rf /opt/tomcat/webapps/ROOT  
  
# tomcat conf  
ADD conf/tomcat-users.xml.tpl /opt/tomcat/conf/  
ADD conf/server.xml.tpl /opt/tomcat/conf/  
# circusd tomcat conf  
ADD circus.d/tomcat.ini.tpl /etc/circus.d/  
# tomcat and circus setup script  
ADD setup.d/setup-tomcat /etc/setup.d/  
  
RUN \  
useradd -u 500 -d /opt/tomcat -s /usr/sbin/nologin tomcat && \  
chown tomcat.tomcat /opt/tomcat -R  
  
ADD app /app  
  
EXPOSE 8080  

