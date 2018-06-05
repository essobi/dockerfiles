# Use latest jboss/wildfly image as the base  
FROM jboss/wildfly:13.0.0.Final  
  
# Run everything below as root user  
USER root  
  
# Clean the metadata  
RUN yum install -y unzip wget && yum -q clean all  
  
## PostgreSQL  
ENV psql_module_dir=$JBOSS_HOME/modules/org/postgresql/main/  
ENV psql_connector_jar=postgresql-jdbc.jar  
RUN mkdir -p ${psql_module_dir}  
RUN wget -O ${psql_connector_jar}
http://search.maven.org/remotecontent\?filepath\=org/postgresql/postgresql/42.2.2/postgresql-42.2.2.jar  
RUN mv ${psql_connector_jar} ${psql_module_dir}  
COPY configuration/xml/psql-module.xml ${psql_module_dir}/module.xml  
  
# Rename the original configuration file  
RUN mv $JBOSS_HOME/standalone/configuration/standalone.xml
$JBOSS_HOME/standalone/configuration/standalone.xml.orig  
  
# WildFly configuration file ready for HTTPS  
ADD configuration/xml/standalone-full-sample.xml
$JBOSS_HOME/standalone/configuration/standalone.xml  
  
# Add the certificate.sh script into
$JBOSS_HOME/standalone/configuration/certs  
ADD configuration/certs/ $JBOSS_HOME/standalone/configuration/certs  
  
# update rights for everything to be jboss user owned  
#RUN chown -R jboss:jboss $JBOSS_HOME/standalone  
# Switch to $JBOSS_HOME/configuration/certs  
WORKDIR /opt/jboss/wildfly/standalone/configuration/certs  
  
# Execute the script to generate self signed certificates  
RUN ./certificate.sh  
  
# Switch to the working dir /opt/jboss/wildfly  
WORKDIR /opt/jboss/wildfly  
  
# Expose default port  
EXPOSE 8080  

