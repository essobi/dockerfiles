FROM jboss/wildfly  
  
RUN touch /opt/jboss/I_AM_HERE_v10  
  
ADD ROOT.war /opt/jboss/wildfly/standalone/deployments/  
  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0",
"-Djboss.server.data.dir=/tmp/jboss/data",
"-Djboss.server.temp.dir=/tmp/jboss/tmp",
"-Djboss.server.log.dir=/tmp/jboss/log"]  

