#  
# Docker image configuration for dsbuilder configured with a locally available  
# mysql database and loaded with the patients example data.  
#  
FROM teiidkomodo/dsbuilder-mysql:latest  
MAINTAINER Teiid-Komodo Community <http://teiiddesigner.jboss.org>  
  
#  
# Env variables  
#  
ENV BIN_DIR /usr/local/bin  
ENV JBOSS_HOME /opt/jboss/wildfly  
ENV MYSQL_USER_NAME admin  
ENV MYSQL_USER_PASS admin  
  
#  
# Change to root user  
#  
USER root  
  
#  
# Add the mysql database scripts and import  
#  
ADD schema/*.sql ./  
RUN ${BIN_DIR}/mysql-exec.sh && \  
mysql -u ${MYSQL_USER_NAME} -p${MYSQL_USER_PASS} \--silent < patients.sql && \  
mysql -u ${MYSQL_USER_NAME} -p${MYSQL_USER_PASS} \--silent < us-states.sql &&
\  
rm -f *.sql  
  
#  
# Add datasource configuration files  
#  
ADD datasources/* ./  
  
#  
# Start wildfly and configure the data sources  
#  
RUN chmod +x ./configure-wildfly-datasources.sh && ./configure-wildfly-
datasources.sh  
  
#  
# These folders are marked as Docker volumes. So they are mounted when docker
runs the final container  
# To have the data persisted across several docker run executions, need to
mount volumes.  
#  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
#  
# The default cmd for this container remains the parent mysql/wildfly exec
command  
#  

