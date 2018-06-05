# Tomcat 8 image  
FROM tomcat:8  
MAINTAINER Andre Nascimento <andreluiznsilva@gmail.com>  
  
ENV JAVA_OPTS -Djava.security.egd=file:/dev/./urandom  
  
ENV RESOURCES=""  
ENV LIBS=""  
RUN apt-get update && apt-get install -y wget && apt-get autoremove && apt-get
autoclean  
RUN echo '<?xml version="1.0" encoding="utf-8"?><tomcat-users><role
rolename="manager-gui"/><user username="admin" password="admin*123"
roles="manager-gui"/></tomcat-users>' > $CATALINA_HOME/conf/tomcat-users.xml
&& \  
env JAVA_OPTS="$JAVA_OPTS"  
  
EXPOSE 8080  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["catalina.sh", "run"]

