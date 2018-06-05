FROM jboss/wildfly  
RUN /opt/jboss/wildfly/bin/add-user.sh admin admin --silent  
RUN /opt/jboss/wildfly/bin/add-user.sh -p binbase -g guest -u binbase -a
--silent  
COPY standalone-full.xml
/opt/jboss/wildfly/standalone/configuration/binbase.xml  
CMD ["/opt/jboss/wildfly/bin/standalone.sh","-c","binbase.xml", "-b",
"0.0.0.0", "-bmanagement", "0.0.0.0"]  

