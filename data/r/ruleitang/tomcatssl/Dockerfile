FROM desiato/tomcat-ssl  
COPY tomcat-users.xml $CATALINA_HOME/conf  
COPY context.xml /usr/local/tomcat/webapps/manager/META-INF  
  
EXPOSE 8443  
VOLUME $CATALINA_HOME/conf  
  
CMD start.sh

