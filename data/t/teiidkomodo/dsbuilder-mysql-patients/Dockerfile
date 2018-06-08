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
rm -f *.sql  
  
#  
# Import the patients zip into the dsbuilder repository  
#  
## TODO - ensure base64 is installed  
ADD patients-service ./patients-service  
RUN yum -y install --setopt=tsflags=nodocs zip && \  
cd patients-service && \  
bash upload-patients.sh  
  
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

