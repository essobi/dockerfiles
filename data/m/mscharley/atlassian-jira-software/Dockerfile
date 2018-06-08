# Build from Ubuntu LTS release.  
FROM isuper/java-oracle:jre_8  
MAINTAINER Matthew Scharley <matt.scharley@gmail.com>  
  
# Variables.  
ENV JIRA_VERSION 7.0.4  
ENV PGSQL_VERSION 9.4-1206  
ENV MYSQL_CONNECTOR_VERSION 5.1.38  
ENV JIRA_HOME /var/atlassian/jira-software  
ENV JIRA_INSTALL /opt/atlassian/jira-software  
  
RUN set -x && \  
mkdir -p ${JIRA_HOME} && \  
chown daemon:daemon ${JIRA_HOME} && chmod 0700 ${JIRA_HOME} && \  
mkdir -p ${JIRA_INSTALL} && cd ${JIRA_INSTALL} && \  
curl -LSs "https://www.atlassian.com/software/jira/downloads/binary/atlassian-
jira-software-${JIRA_VERSION}-jira-${JIRA_VERSION}.tar.gz" -o - | tar xz
--strip-components=1 --no-same-owner && \  
curl -LSs
"https://jdbc.postgresql.org/download/postgresql-${PGSQL_VERSION}-jdbc42.jar"
-o "${JIRA_INSTALL}/lib/postgresql-${PGSQL_VERSION}-jdbc42.jar" && \  
curl -LSs "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.tar.gz" | tar xz --directory
"${JIRA_INSTALL}/lib" \--strip-components=1 --no-same-owner "mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}-bin.jar" && \  
chmod -R 700 "${JIRA_INSTALL}/conf" "${JIRA_INSTALL}/logs"
"${JIRA_INSTALL}/temp" "${JIRA_INSTALL}/work" && \  
chown -R daemon:daemon "${JIRA_INSTALL}/conf" "${JIRA_INSTALL}/logs"
"${JIRA_INSTALL}/temp" "${JIRA_INSTALL}/work"  
  
# Setup user account.  
USER daemon:daemon  
  
# Expose ports and working directories.  
EXPOSE 8080  
VOLUME ["${JIRA_HOME}"]  
  
# Setup the executable itself.  
WORKDIR "${JIRA_HOME}"  
ENTRYPOINT ["/opt/atlassian/jira-software/bin/start-jira.sh", "-fg"]  

