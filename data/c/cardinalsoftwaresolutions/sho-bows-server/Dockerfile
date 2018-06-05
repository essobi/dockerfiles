FROM tomcat:8.0  
RUN curl http://central.maven.org/maven2/mysql/mysql-connector-
java/5.1.38/mysql-connector-java-5.1.38.jar -o $CATALINA_HOME/lib/mysql-
connector-java-5.1.38.jar  
  
COPY shobows-api.war /usr/local/tomcat/webapps/  
  
CMD ["catalina.sh", "run"]

