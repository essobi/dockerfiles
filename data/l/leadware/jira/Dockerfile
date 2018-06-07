# Leadware  
#  
# JIRA Server Dockerfile  
# https://bitbucket.org/leadware/dockerfile-jira  
# https://jetune@bitbucket.org/leadware/dockerfile-jira.git  
# git@bitbucket.org:leadware/dockerfile-jira.git  
#  
# Pull base image.  
FROM leadware/oracle-java8:latest  
  
# Maintainer  
MAINTAINER Jean-Jacques ETUNÈ NGI<jetune@leadware.net>  
  
# JIRA VERSION  
ARG JIRA_VERSION=7.6.1  
# JIRA INSTALL DIR  
ARG JIRA_INSTALL=/opt/atlassian/jira  
  
# JIRA HOME DIR  
ARG JIRA_HOME=/var/atlassian/jira  
  
# Leadware Custom Data Home  
ARG LW_CUSTOM_DATA_HOME=/var/leadware/jira  
  
# JIRA USER  
ARG JIRA_USER="jira"  
# JIRA GROUP  
ARG JIRA_GROUP="jira"  
# MYSQL VERSION  
ARG MYSQL_VERSION=5.1.45  
# POSGRES JDBC DRIVER VERSION  
ARG POSTGRES_JDBC_DRIVER_VERSION=42.1.4  
# Add Entry point script file  
ADD entrypoint.sh /leadware-entrypoint.sh  
  
# Add Mysql DB Configuration  
ADD dbconfig-mysql.xml /dbconfig-mysql.xml  
  
# Add Postgres DB Configuration  
ADD dbconfig-postgres.xml /dbconfig-postgres.xml  
  
# Add Tomcat Configuration  
ADD server.xml /server.xml  
  
# Add Tomcat Configuration  
ADD secured-server.xml /secured-server.xml  
  
# Add Tomcat Configuration  
ADD secured-web.xml /secured-web.xml  
  
# Add Mysql DB Configuration  
ADD setenv.sh /setenv.sh  
  
# Run commands  
RUN \  
  
# Update APT  
apt-get update -y && \  
  
# Install CURL  
apt-get install -y curl && \  
  
# Create Required Directories  
mkdir -p ${LW_CUSTOM_DATA_HOME} ${JIRA_INSTALL} "${JIRA_HOME}"
"${JIRA_HOME}/caches/indexes" "$LW_CUSTOM_DATA_HOME/ssl" && \  
  
# Move JIRA DB Config custom dir  
mv /dbconfig-postgres.xml /dbconfig-mysql.xml /server.xml /secured-server.xml
/secured-web.xml $LW_CUSTOM_DATA_HOME && \  
  
# Download JIRA archive  
curl -Ls "https://product-
downloads.atlassian.com/software/jira/downloads/atlassian-jira-
software-${JIRA_VERSION}.tar.gz" | tar -xz --directory "${JIRA_INSTALL}"
\--strip-components=1 \--no-same-owner && \  
  
# Set JIRA Work DIR on jira.home  
echo -e "\njira.home=$JIRA_HOME" >> "${JIRA_INSTALL}/atlassian-jira/WEB-
INF/classes/jira-application.properties" && \  
  
# Download Mysql Connector  
curl -Ls http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_VERSION}.tar.gz | tar xz --directory "${JIRA_INSTALL}/lib"
\--strip-components=1 \--no-same-owner "mysql-connector-
java-${MYSQL_VERSION}/mysql-connector-java-${MYSQL_VERSION}-bin.jar" && \  
  
# Delete Mysql Archive  
rm -Rf mysql-connector-java-${MYSQL_VERSION}.tar.gz && \  
  
# Download Postgres JDBC Connector  
wget -O ${JIRA_INSTALL}/lib/postgresql-${POSTGRES_JDBC_DRIVER_VERSION}.jar
https://jdbc.postgresql.org/download/postgresql-${POSTGRES_JDBC_DRIVER_VERSION}.jar
&& \  
  
# Move JIRA Set ENV Script to bin dir  
mv /setenv.sh $JIRA_INSTALL/bin && \  
  
# Create dedicated group  
groupadd ${JIRA_GROUP} && \  
  
# Create dedicated user  
useradd --create-home --comment "Account for running JIRA Software" -g
${JIRA_GROUP} --shell /bin/bash ${JIRA_USER} && \  
  
# Change the Install directory wonership to $JIRA_USER  
chown -R ${JIRA_USER} ${JIRA_INSTALL} && \  
  
# Change the install directory access mode  
chmod -R u=rwx,go-rwx ${JIRA_INSTALL} && \  
  
# Change the Home directory wonership to $JIRA_USER  
chown -R ${JIRA_USER} ${JIRA_HOME} && \  
  
# Change the Home directory access mode  
chmod -R u=rwx,go-rwx ${JIRA_HOME} && \  
  
# Set execution right to every body  
chmod 755 /leadware-entrypoint.sh  
  
# Expose HTTP Ports  
EXPOSE 8080 8443 80 443  
# Set ENV JIRA_INSTALL  
ENV JIRA_INSTALL $JIRA_INSTALL  
  
# Set ENV LW_CUSTOM_DATA_HOME  
ENV LW_CUSTOM_DATA_HOME $LW_CUSTOM_DATA_HOME  
  
# Set ENV LW_CUSTOM_DATA_SSL_HOME  
ENV LW_CUSTOM_DATA_SSL_HOME $LW_CUSTOM_DATA_HOME/ssl  
  
# Set ENV JIRA_SSL_DIR  
ENV JIRA_CONF_DIR $JIRA_INSTALL/conf  
  
# Set ENV JIRA_HOME  
ENV JIRA_HOME $JIRA_HOME  
  
# Set working dir  
WORKDIR $JIRA_HOME  
  
# Declare Volumes  
VOLUME ["/var/atlassian/jira", "/opt/atlassian/jira/logs",
"/var/leadware/jira/ssl"]  
  
# Run Leadware Entry point.  
CMD ["/leadware-entrypoint.sh"]  

