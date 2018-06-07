FROM tomcat:8.0-jre8  
MAINTAINER De1mos <de1m0s242@gmail.com>  
  
RUN apt-get update && apt-get install -y gettext && apt-get install -y --no-
install-recommends openjfx  
  
COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml.tmpl  
COPY context.xml /usr/local/tomcat/conf/  
COPY tomcat-manager-web.xml /usr/local/tomcat/webapps/manager/WEB-INF/web.xml  
COPY postgresql-jdbc4.jar /usr/local/tomcat/lib/postgresql.jar  
COPY setenv.sh /usr/local/tomcat/bin/  
COPY entrypoint.sh /usr/local/tomcat/bin/  
  
VOLUME /usr/local/tomcat/webapps  
VOLUME /usr/local/tomcat/logs  
VOLUME /var/external-files  
  
ENV JAVA_XMS -Xms256m  
ENV JAVA_XMX -Xmx378m  
  
ENTRYPOINT ["/usr/local/tomcat/bin/entrypoint.sh"]  
  
CMD ["catalina.sh", "run"]  

