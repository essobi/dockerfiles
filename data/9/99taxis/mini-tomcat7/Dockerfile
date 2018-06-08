FROM 99taxis/mini-java8:1.0  
MAINTAINER "F. Balancin" <balancin@gmail.com>  
  
# Expose web port  
EXPOSE 8080  
# Tomcat Version  
ENV TOMCAT_VERSION_MAJOR 7  
ENV TOMCAT_VERSION_FULL 7.0.64  
# Download and install  
RUN apk add --update curl &&\  
curl -LO
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_VERSION_MAJOR}/v${TOMCAT_VERSION_FULL}/bin/apache-
tomcat-${TOMCAT_VERSION_FULL}.tar.gz &&\  
curl -LO
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_VERSION_MAJOR}/v${TOMCAT_VERSION_FULL}/bin/apache-
tomcat-${TOMCAT_VERSION_FULL}.tar.gz.md5 &&\  
md5sum -c apache-tomcat-${TOMCAT_VERSION_FULL}.tar.gz.md5 &&\  
gunzip -c apache-tomcat-${TOMCAT_VERSION_FULL}.tar.gz | tar -xf - -C /opt &&\  
rm -f apache-tomcat-${TOMCAT_VERSION_FULL}.tar.gz apache-
tomcat-${TOMCAT_VERSION_FULL}.tar.gz.md5 &&\  
ln -s /opt/apache-tomcat-${TOMCAT_VERSION_FULL} /opt/tomcat &&\  
rm -rf /opt/tomcat/webapps/examples /opt/tomcat/webapps/docs &&\  
apk del curl &&\  
rm -rf /var/cache/apk/*  
  
# Configuration  
# ADD tomcat-users.xml /opt/tomcat/conf/  
RUN addgroup -S tomcat && adduser -S -g tomcat tomcat  
RUN chown -R tomcat:tomcat /opt/tomcat  
RUN sed -i 's/52428800/5242880000/g' /opt/tomcat/webapps/manager/WEB-
INF/web.xml  
  
# Set environment  
ENV CATALINA_HOME /opt/tomcat  
  
# Launch Tomcat on startup  
CMD ${CATALINA_HOME}/bin/catalina.sh run  

