FROM maven  
CMD mvn install  
  
FROM jboss/wildfly  
CMD ["cp",
"/usr/src/app/target/movieplex7-1.0-SNAPSHOT.war","/opt/jboss/wildfly/standalone/deployments/"]  
RUN /opt/jboss/wildfly/bin/add-user.sh admin Admin --silent  
  
EXPOSE 8080 9990  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]  

