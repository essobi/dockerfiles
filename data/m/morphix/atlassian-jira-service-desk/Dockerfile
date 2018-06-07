## Based off https://github.com/cptactionhank/docker-atlassian-jira-service-
desk  
FROM morphix/debian-jessie-oracle-jdk-8  
# Configuration variables.  
ENV JIRA_HOME /var/atlassian/jira  
ENV JIRA_INSTALL /opt/atlassian/jira  
ENV JIRA_VERSION 7.1.8  
ENV APP_VERSION 3.2.7  
ENV JIRASD_DOWNLOAD_URL
https://www.atlassian.com/software/jira/downloads/binary/atlassian-
servicedesk-${APP_VERSION}.tar.gz  
  
ENV MYSQL_VERSION 5.1.40  
ENV MYSQL_DRIVER_DOWNLOAD_URL
http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_VERSION}.tar.gz  
  
# Install Atlassian JIRA and helper tools and setup initial home  
# directory structure.  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends libtcnative-1
xmlstarlet curl \  
&& apt-get clean \  
&& mkdir -p "${JIRA_HOME}" \  
&& mkdir -p "${JIRA_HOME}/caches/indexes" \  
&& chmod -R 700 "${JIRA_HOME}" \  
&& chown -R daemon:daemon "${JIRA_HOME}" \  
&& mkdir -p "${JIRA_INSTALL}/conf/Catalina" \  
&& curl -Ls "${JIRASD_DOWNLOAD_URL}" | tar -xz --directory "${JIRA_INSTALL}"
\--strip-components=1 --no-same-owner \  
&& curl -Ls "${MYSQL_DRIVER_DOWNLOAD_URL}" | tar -xz --directory
"${JIRA_INSTALL}/lib" \--strip-components=1 --no-same-owner "mysql-connector-
java-${MYSQL_VERSION}/mysql-connector-java-${MYSQL_VERSION}-bin.jar" \  
&& chmod -R 700 "${JIRA_INSTALL}/conf" \  
&& chmod -R 700 "${JIRA_INSTALL}/logs" \  
&& chmod -R 700 "${JIRA_INSTALL}/temp" \  
&& chmod -R 700 "${JIRA_INSTALL}/work" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/conf" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/logs" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/temp" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/work" \  
&& echo -e "\njira.home=$JIRA_HOME" >> "${JIRA_INSTALL}/atlassian-jira/WEB-
INF/classes/jira-application.properties" \  
&& touch -d "@0" "${JIRA_INSTALL}/conf/server.xml"  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
USER daemon:daemon  
  
# Expose default HTTP connector port.  
EXPOSE 8080  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs.  
VOLUME ["/var/atlassian/jira", "/opt/atlassian/jira/logs"]  
  
# Set the default working directory as the installation directory.  
WORKDIR /var/atlassian/jira  
  
COPY "docker-entrypoint.sh" "/"  
ENTRYPOINT ["sh","/docker-entrypoint.sh"]  
  
# Run Atlassian JIRA as a foreground process by default.  
CMD ["/opt/atlassian/jira/bin/catalina.sh", "run"]  

