#
-------------------------------------------------------------------------------------------------------------------------  
#  
# ATLASSIAN JIRA STANDALONE SERVER  
#  
# Thanks to original project example :
https://github.com/cptactionhank/docker-atlassian-jira  
#  
# @see
https://confluence.atlassian.com/display/JIRA/Installing+JIRA+from+an+Archive+File+on+Windows%2C+Linux+or+Solaris  
# @see
https://confluence.atlassian.com/display/JIRA/JIRA+Installation+Directory  
# @see
https://confluence.atlassian.com/display/JIRA/Setting+your+JIRA+Home+Directory  
# @see
https://confluence.atlassian.com/display/JIRA/Connecting+JIRA+to+PostgreSQL  
# @see https://confluence.atlassian.com/display/JIRA/Supported+Platforms  
# @see http://www.cyberciti.biz/faq/linux-unix-extracting-specific-files/  
#  
#
-------------------------------------------------------------------------------------------------------------------------  
# Base image  
FROM airdock/oracle-jdk:1.8  
# Maintainer  
MAINTAINER alban.montaigu@gmail.com  
  
  
# Configuration variables.  
ENV DEBIAN_FRONTEND="noninteractive" \  
JIRA_HOME="/var/local/atlassian/jira" \  
JIRA_INSTALL="/usr/local/atlassian/jira" \  
JIRA_VERSION="7.3.0" \  
CATALINA_OPTS="-Xms128m -Xmx1024m -Datlassian.plugins.enable.wait=300"  
# Base system update (isolated to not reproduce each time)  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends libtcnative-1
xmlstarlet wget \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
# Install Atlassian JIRA and helper tools and setup initial home  
# directory structure (isolated to not reproduce each time).  
RUN set -x \  
&& mkdir -p "${JIRA_HOME}" \  
&& chmod -R 700 "${JIRA_HOME}" \  
&& chown -R daemon:daemon "${JIRA_HOME}" \  
&& mkdir -p "${JIRA_INSTALL}/conf/Catalina" \  
&& wget -P /tmp --no-check-certificate
"https://downloads.atlassian.com/software/jira/downloads/atlassian-jira-
software-${JIRA_VERSION}.tar.gz" -nv \  
&& tar xz -f "/tmp/atlassian-jira-software-${JIRA_VERSION}.tar.gz"
\--directory "${JIRA_INSTALL}" \--strip-components=1 --no-same-owner \  
&& rm -rf "/tmp/atlassian-jira-software-${JIRA_VERSION}.tar.gz" \  
&& chmod -R 700 "${JIRA_INSTALL}/conf" \  
&& chmod -R 700 "${JIRA_INSTALL}/logs" \  
&& chmod -R 700 "${JIRA_INSTALL}/temp" \  
&& chmod -R 700 "${JIRA_INSTALL}/work" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/conf" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/logs" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/temp" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/work"  
  
# Custom jira configuration (isolated to not reproduce each time)  
RUN set -x \  
&& echo -e "\njira.home=$JIRA_HOME" >> "${JIRA_INSTALL}/atlassian-jira/WEB-
INF/classes/jira-application.properties"  
  
# PostgreSQL connector for jira (isolated to not reproduce each time)  
RUN set -x \  
&& wget -P "${JIRA_INSTALL}/lib/postgresql-9.4-1202.jdbc41.jar" \--no-check-
certificate
"https://jdbc.postgresql.org/download/postgresql-9.4-1202.jdbc41.jar" -nv  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
USER daemon:daemon  
  
  
# Expose default HTTP connector port.  
EXPOSE 8080  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs.  
VOLUME ["/var/local/atlassian/jira"]  
  
# Set the default working directory as the installation directory.  
WORKDIR ${JIRA_INSTALL}  
  
# Run Atlassian JIRA as a foreground process by default.  
CMD ["./bin/start-jira.sh", "-fg"]  

