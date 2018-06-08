FROM java:7  
MAINTAINER Marco Re "ingmarcore+docker@gmail.com"  
# Set some variables  
ENV LIFERAY_HOME /var/liferay-home  
ENV CATALINA_OPTS -Dfile.encoding=UTF8 -Djava.net.preferIPv4Stack=true
-Dorg.apache.catalina.loader.WebappClassLoader.ENABLE_CLEAR_REFERENCES=false
-Duser.timezone=Europe/Paris -Xmx1024m -XX:MaxPermSize=256m  
  
# Download and unzip Liferay bundle  
RUN (cd /tmp && \  
wget
http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/6.2.2%20GA3/liferay-
portal-tomcat-6.2-ce-ga3-20150103155803016.zip -O liferay.zip && \  
unzip liferay.zip -d /opt && \  
rm -f liferay.zip)  
  
ADD conf/portal-bundle.properties /opt/liferay-portal-6.2-ce-ga3/portal-
bundle.properties  
  
EXPOSE 8080  
ENTRYPOINT ["/opt/liferay-portal-6.2-ce-ga3/tomcat-7.0.42/bin/catalina.sh"]  
CMD ["run"]  

