FROM jboss/wildfly  
ADD igdoc.services.validation-1.0.0-SNAPSHOT.war
/opt/jboss/wildfly/standalone/deployments/  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]

