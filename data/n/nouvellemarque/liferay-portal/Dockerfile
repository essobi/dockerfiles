#FROM nouvellemarque/apache-maven:3.3.9-jdk-7  
FROM nouvellemarque/oracle-jdk:7  
MAINTAINER Erik Allais <e.allais@nouvellemarque.com>  
  
# Install Liferay Portal  
RUN wget
http://ufpr.dl.sourceforge.net/project/lportal/Liferay%20Portal/6.2.5%20GA6/liferay-
portal-tomcat-6.2-ce-ga6-20160112152609836.zip && \  
mkdir /opt && \  
unzip liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip -d /opt && \  
rm liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip && \  
ln -s /opt/liferay-portal-6.2-ce-ga6 /opt/liferay-portal && \  
ln -s /opt/liferay-portal/$(ls -1 /opt/liferay-portal | grep tomcat-)
/opt/liferay-portal/tomcat && \  
mkdir /opt/liferay-portal/deploy && \  
chown -R 1000:1000 /opt/liferay-portal/* && \  
echo "#!/bin/sh" > /usr/bin/liferay && \  
echo "/opt/liferay-portal/tomcat/bin/catalina.sh run" >> /usr/bin/liferay && \  
chmod +x /usr/bin/liferay && \  
rm -rf /opt/liferay-portal/tomcat/temp/* \  
/opt/liferay-portal/tomcat/work/* && \  
rm -rf /tmp/*  
  
# Apply patches  
COPY ./rootfs/opt/liferay-portal/tomcat/webapps/resources-importer-web/META-
INF/custom_jsps/html/portlet/journal/article_toolbar.jsp /opt/liferay-
portal/tomcat/webapps/resources-importer-web/META-
INF/custom_jsps/html/portlet/journal/article_toolbar.jsp  
  
CMD /usr/bin/liferay  
  
EXPOSE 8080 8009  

