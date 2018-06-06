FROM openjdk:8  
MAINTAINER Remon Lam [remon@containerstack.io]  
  
# Configuration variables.  
ENV JIRA_HOME /var/atlassian/jira  
ENV JIRA_INSTALL /opt/atlassian/jira  
# Check Jira version @ https://confluence.atlassian.com/jirasoftware/jira-
software-release-notes-776821069.html  
ENV JIRA_VERSION 7.9.2  
# Check Connector/J version @ http://dev.mysql.com/downloads/connector/j/ it
should be 5.1.30, testing with latest release  
ENV MYSQL_CONJ_VERSION 5.1.42  
# Install Atlassian JIRA and helper tools and setup initial home  
# directory structure.  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends libtcnative-1
xmlstarlet \  
&& apt-get clean \  
&& mkdir -p "${JIRA_HOME}" \  
&& mkdir -p "${JIRA_HOME}/caches/indexes" \  
&& chmod -R 700 "${JIRA_HOME}" \  
&& chown -R daemon:daemon "${JIRA_HOME}" \  
&& mkdir -p "${JIRA_INSTALL}/conf/Catalina" \  
&& curl -Ls
"https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-
software-${JIRA_VERSION}.tar.gz" | tar -xz --directory "${JIRA_INSTALL}"
\--strip-components=1 --no-same-owner \  
&& curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_CONJ_VERSION}.tar.gz" | tar -xz --directory "${JIRA_INSTALL}/lib"
\--strip-components=1 --no-same-owner "mysql-connector-
java-${MYSQL_CONJ_VERSION}/mysql-connector-java-${MYSQL_CONJ_VERSION}-bin.jar"
\  
&& chmod -R 700 "${JIRA_INSTALL}/conf" \  
&& chmod -R 700 "${JIRA_INSTALL}/logs" \  
&& chmod -R 700 "${JIRA_INSTALL}/temp" \  
&& chmod -R 700 "${JIRA_INSTALL}/work" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/conf" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/logs" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/temp" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/work" \  
&& sed --in-place "s/java version/openjdk version/g"
"${JIRA_INSTALL}/bin/check-java.sh" \  
&& echo -e "\njira.home=$JIRA_HOME" >> "${JIRA_INSTALL}/atlassian-jira/WEB-
INF/classes/jira-application.properties" \  
&& touch -d "@0" "${JIRA_INSTALL}/conf/server.xml"  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
#  
# Make sure that the host mount point have the correct user settings.  
USER daemon:daemon  
  
# Expose default HTTP connector port.  
EXPOSE 8080  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs.  
VOLUME ["/var/atlassian/jira", "/opt/atlassian/jira/logs"]  
  
# Set the default working directory as the installation directory.  
WORKDIR /var/atlassian/jira  
  
COPY "entrypoint.sh" "/"  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Run Atlassian JIRA as a foreground process by default.  
CMD ["/opt/atlassian/jira/bin/catalina.sh", "run"]  

