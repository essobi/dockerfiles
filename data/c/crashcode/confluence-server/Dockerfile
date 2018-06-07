FROM ubuntu:latest  
MAINTAINER Chad Jones <chad@crashcode.org>  
  
# Setup useful environment variables  
ENV CONFLUENCE_HOME /var/atlassian/application-data/confluence  
ENV CONFLUENCE_INSTALL /opt/atlassian/confluence  
ENV CONF_VERSION 6.7.1  
LABEL Description="This image is used to start Atlassian Confluence"
Vendor="Atlassian" Version="${CONF_VERSION}"  
  
ENV CONFLUENCE_DOWNLOAD_URL
http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONF_VERSION}.tar.gz  
  
ENV MYSQL_VERSION 5.1.38  
ENV MYSQL_DRIVER_DOWNLOAD_URL
http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_VERSION}.tar.gz  
  
ENV CONF_REMOTE_DEBUG false  
ENV RAM_MIN 1024  
ENV RAM_MAX 2048  
ENV DEBUG_PORT 5005  
ENV HTTPS false  
ENV IMPORTCERT false  
ENV IMPORTPATH /var/certificates  
  
ENV PROXY_NAME false  
  
ENV WAIT false  
ENV WAIT_COMMAND none  
ENV WAIT_SLEEP 3  
ENV WAIT_LOOPS 10  
ENV BACKUP_HOST false  
ENV BACKUP_PATH false  
ENV BACKUP_USER false  
ENV BACKUP_KEY_FILE /tmp/id_rsa  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
  
# Install Atlassian Confluence and helper tools and setup initial home  
# directory structure.  
# dumb-init is used to give proper signal handling to the app inside Docker  
RUN set -x \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
C2518248EEA14886 \  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu/ precise main" >
/etc/apt/sources.list.d/java.list \  
&& echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-
set-selections \  
&& echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-set-
selections \  
&& apt-get update \  
&& apt-get install -y \  
oracle-java8-installer \  
rsync \  
openssh-client \  
&& apt-get clean \  
&& echo -n > /var/lib/apt/extended_states \  
&& set -x \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends tzdata libtcnative-1
xmlstarlet ssh wget curl sed unzip \  
&& apt-get clean \  
&& wget -nv -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 \  
&& chmod +x /usr/local/bin/dumb-init \  
&& mkdir -p "${CONFLUENCE_HOME}" \  
&& chmod -R 700 "${CONFLUENCE_HOME}" \  
&& chown ${RUN_USER}:${RUN_GROUP} "${CONFLUENCE_HOME}" \  
&& mkdir -p "${CONFLUENCE_INSTALL}/conf" \  
&& curl -Ls "${CONFLUENCE_DOWNLOAD_URL}" | tar -xz --directory
"${CONFLUENCE_INSTALL}" \--strip-components=1 --no-same-owner \  
&& curl -Ls "${MYSQL_DRIVER_DOWNLOAD_URL}" | tar -xz --directory
"${CONFLUENCE_INSTALL}/confluence/WEB-INF/lib" \--strip-components=1 --no-
same-owner "mysql-connector-java-${MYSQL_VERSION}/mysql-connector-
java-${MYSQL_VERSION}-bin.jar" \  
&& chmod -R 700 "${CONFLUENCE_INSTALL}/conf" \  
&& chmod -R 700 "${CONFLUENCE_INSTALL}/temp" \  
&& chmod -R 700 "${CONFLUENCE_INSTALL}/logs" \  
&& chmod -R 700 "${CONFLUENCE_INSTALL}/work" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} "${CONFLUENCE_INSTALL}/conf" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} "${CONFLUENCE_INSTALL}/temp" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} "${CONFLUENCE_INSTALL}/logs" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} "${CONFLUENCE_INSTALL}/work" \  
&& chown ${RUN_USER}: /usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts \  
&& echo -e "\nconfluence.home=${CONFLUENCE_HOME}" >>
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
"${CONFLUENCE_INSTALL}/conf/server.xml" \  
&& touch -d "@0" "${CONFLUENCE_INSTALL}/conf/server.xml"  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
USER ${RUN_USER}:${RUN_GROUP}  
  
# Expose default HTTP connector port.  
EXPOSE 8090  
EXPOSE 8091  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs.  
VOLUME ["${CONFLUENCE_INSTALL}", "${CONFLUENCE_HOME}"]  
  
# Set the default working directory as the Confluence installation directory.  
WORKDIR ${CONFLUENCE_INSTALL}  
  
# Run Atlassian Confluence as a foreground process by default.  
CMD ["/usr/local/bin/dumb-init", "./bin/catalina.sh", "run"]  
  

