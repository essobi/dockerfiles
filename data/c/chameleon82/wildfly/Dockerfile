FROM jboss/wildfly  
  
COPY ojdbc7.jar /var/tmp  
  
RUN /opt/jboss/wildfly/bin/jboss-cli.sh \--command="module add
--name=com.oracle.jdbc --resources=/var/tmp/ojdbc7.jar
--dependencies=javax.api,javax.transaction.api" && \  
/opt/jboss/wildfly/bin/jboss-cli.sh \--commands=embed-
server,/subsystem=datasources/jdbc-driver=oracle:add\\(driver-
name=ojbdc7,driver-module-name=com.oracle.jdbc,driver-xa-datasource-class-
name=oracle.jdbc.xa.client.OracleXADataSource\\),stop-embedded-server && \  
/opt/jboss/wildfly/bin/add-user.sh admin admin --silent  
  
EXPOSE 9990 8080  
  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]  

