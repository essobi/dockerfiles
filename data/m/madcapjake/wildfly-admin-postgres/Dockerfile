# Use latest jboss/base-jdk:7 image as the base  
FROM jboss/base-jdk:8  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 8.2.0.Final  
  
# Add the WildFly distribution to /opt, and make wildfly the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd $HOME && curl
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar zx && mv $HOME/wildfly-$WILDFLY_VERSION $HOME/wildfly  
  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/jboss/wildfly  
  
# Expose the ports we're interested in  
EXPOSE 8080 9090  
# Get Postgres stuff  
RUN curl -o /tmp/psql-jdbc.jar
https://jdbc.postgresql.org/download/postgresql-9.4-1201.jdbc41.jar  
RUN curl -o /tmp/postgis-jdbc.jar http://postgis.net/stuff/postgis-
jdbc-2.1.3.jar  
ADD config.sh /tmp/  
ADD batch.cli /tmp/  
  
# Set up modules  
RUN /tmp/config.sh  
  
# Add admin user  
RUN /opt/jboss/wildfly/bin/add-user.sh admin Admin#007 --silent  
  
# Use the modules  
# ATTN: Configuring standalone via jboss_cli instead  
# ADD standalone.xml /opt/jboss/wildfly/standalone/configuration/  
# Remove standalone_xml_history/current directory  
RUN rm -rf
/opt/jboss/wildfly/standalone/configuration/standalone_xml_history/current  
  
# CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0",
"-bmanagement", "0.0.0.0" "-Djboss.management.http.port" "9090"]  
CMD /opt/jboss/wildfly/bin/standalone.sh -b 0.0.0.0 -bmanagement 0.0.0.0
-Djboss.management.http.port=9090  

