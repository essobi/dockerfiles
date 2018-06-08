FROM jeanblanchard/tomcat:8  
MAINTAINER Justin Carter justin.w.carter@gmail.com  
  
ENV LUCEE_VERSION 4.5.1.023  
RUN curl -L http://bitbucket.org/lucee/lucee/downloads/lucee-$LUCEE_VERSION-
jars.zip -o /tmp/lucee-jars.zip && \  
mkdir -p /opt/lucee/lib && \  
unzip -o /tmp/lucee-jars.zip -d /opt/lucee/lib && \  
rm -rf /tmp/* /opt/tomcat/webapps  
  
COPY tomcat/catalina.properties /opt/tomcat/conf/catalina.properties  
COPY tomcat/server.xml /opt/tomcat/conf/server.xml  
COPY tomcat/web.xml /opt/tomcat/conf/web.xml  
  
COPY www /var/www  
  
EXPOSE 8080  
CMD ["/opt/tomcat/bin/catalina.sh","run"]  

