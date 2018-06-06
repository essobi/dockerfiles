#
-------------------------------------------------------------------------------------------------------------------------  
#  
# ATLASSIAN CONFLUENCE STANDALONE SERVER  
#  
# Thanks to original project example :
https://registry.hub.docker.com/u/cptactionhank/atlassian-
confluence/dockerfile/  
#  
# @see
https://confluence.atlassian.com/display/DOC/Installing+Confluence+on+Linux+from+Archive+File  
# @see https://confluence.atlassian.com/display/DOC/Supported+Platforms  
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
CONFLUENCE_HOME="/var/local/atlassian/confluence" \  
CONFLUENCE_INSTALL="/usr/local/atlassian/confluence" \  
CONFLUENCE_VERSION="6.0.3"  
# Base system update (isolated to not reproduce each time)  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends libtcnative-1
xmlstarlet wget \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
  
# Install Atlassian CONFLUENCE and helper tools and setup initial home  
# directory structure (isolated to not reproduce each time).  
RUN set -x \  
&& mkdir -p "${CONFLUENCE_HOME}" \  
&& chmod -R 700 "${CONFLUENCE_HOME}" \  
&& chown -R daemon:daemon "${CONFLUENCE_HOME}" \  
&& mkdir -p "${CONFLUENCE_INSTALL}/conf/Catalina" \  
&& wget -P /tmp --no-check-certificate
"https://downloads.atlassian.com/software/confluence/downloads/atlassian-
confluence-${CONFLUENCE_VERSION}.tar.gz" -nv \  
&& tar xz -f "/tmp/atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz"
\--directory "${CONFLUENCE_INSTALL}" \--strip-components=1 \--no-same-owner \  
&& rm -rf "/tmp/atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz" \  
&& chmod -R 700 "${CONFLUENCE_INSTALL}/conf" \  
&& chmod -R 700 "${CONFLUENCE_INSTALL}/logs" \  
&& chmod -R 700 "${CONFLUENCE_INSTALL}/temp" \  
&& chmod -R 700 "${CONFLUENCE_INSTALL}/work" \  
&& chown -R daemon:daemon "${CONFLUENCE_INSTALL}/conf" \  
&& chown -R daemon:daemon "${CONFLUENCE_INSTALL}/logs" \  
&& chown -R daemon:daemon "${CONFLUENCE_INSTALL}/temp" \  
&& chown -R daemon:daemon "${CONFLUENCE_INSTALL}/work"  
# Custom confluence configuration (isolated to not reproduce each time)  
RUN set -x \  
&& echo -e "\nconfluence.home=$CONFLUENCE_HOME" >>
"${CONFLUENCE_INSTALL}/confluence/WEB-INF/classes/confluence-init.properties"
\  
&& xmlstarlet ed --inplace \  
\--delete "Server/@debug" \  
\--delete "Server/Service/Connector/@debug" \  
\--delete "Server/Service/Connector/@useURIValidationHack" \  
\--delete "Server/Service/Connector/@minProcessors" \  
\--delete "Server/Service/Connector/@maxProcessors" \  
\--delete "Server/Service/Engine/@debug" \  
\--delete "Server/Service/Engine/Host/@debug" \  
\--delete "Server/Service/Engine/Host/Context/@debug" \  
"${CONFLUENCE_INSTALL}/conf/server.xml"  
# PostgreSQL connector for confluence (isolated to not reproduce each time)  
RUN set -x \  
&& wget -P "${CONFLUENCE_INSTALL}/lib/postgresql-9.4-1202.jdbc41.jar" \--no-
check-certificate
"https://jdbc.postgresql.org/download/postgresql-9.4-1202.jdbc41.jar" -nv  
  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
USER daemon:daemon  
  
  
# Expose default HTTP connector port.  
EXPOSE 8090  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs.  
VOLUME ["/var/local/atlassian/confluence"]  
  
  
# Set the default working directory as the installation directory.  
WORKDIR ${CONFLUENCE_INSTALL}  
  
  
# Run Atlassian CONFLUENCE as a foreground process by default.  
CMD ["./bin/start-confluence.sh", "-fg"]  

