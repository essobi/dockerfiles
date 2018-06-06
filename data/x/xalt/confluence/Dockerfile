FROM ubuntu:latest  
MAINTAINER Philipp Goellner <philipp@goellner.it>, Philipp Goellner
<philipp.goellner@xaltbc.de>  
  
# setup useful environment variables  
ENV CONF_HOME /var/atlassian/confluence  
ENV CONF_INSTALL /opt/atlassian/confluence  
ENV CONF_VERSION 6.3.4  
ENV CONF_URL
http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONF_VERSION}.tar.gz  
  
ENV MYSQL_DRIVER_VERSION 5.1.38  
ENV MYSQL_DRIVER_URL http://dev.mysql.com/get/Downloads/Connector-J/mysql-
connector-java-${MYSQL_DRIVER_VERSION}.tar.gz  
  
ENV CONF_REMOTE_DEBUG false  
ENV RAM_MIN 1024  
ENV RAM_MAX 2048  
ENV DEBUG_PORT 5005  
ENV HTTPS false  
ENV IMPORTCERT false  
ENV IMPORTPATH /var/certificates  
  
ENV PROXY_NAME false  
  
ENV RUN_USER daemon  
  
ENV NEWRELIC_VERSION 3.31.1  
ENV NEWRELIC_APP_NAME confluence-docker  
ENV NEWRELIC_LICENSE unknown  
  
ENV WAIT false  
ENV WAIT_COMMAND none  
ENV WAIT_SLEEP 3  
ENV WAIT_LOOPS 10  
ENV TIME_ZONE false  
  
ENV BACKUP_HOST false  
ENV BACKUP_PATH false  
ENV BACKUP_USER false  
ENV BACKUP_KEY_FILE /tmp/id_rsa  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886
\  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu/ precise main" >
/etc/apt/sources.list.d/java.list \  
&& echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-
set-selections \  
&& echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-set-
selections \  
&& apt-get update --quiet \  
&& apt-get install --quiet --no-install-recommends -y \  
curl \  
libtcnative-1 \  
mysql-client \  
openssh-client \  
oracle-java8-installer \  
rsync \  
sed \  
unzip \  
wget \  
xmlstarlet \  
&& apt-get clean \  
&& echo -n > /var/lib/apt/extended_states \  
&& mkdir -p "${CONF_HOME}" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} "${CONF_HOME}" \  
&& mkdir -p "${CONF_INSTALL}" \  
&& curl -Lsk "${CONF_URL}" | tar -xz --directory "${CONF_INSTALL}" \--strip-
components=1 \  
&& curl -Lsk "${MYSQL_DRIVER_URL}" | tar -xz --directory
"${CONF_INSTALL}/confluence/WEB-INF/lib" \--strip-components=1 --no-same-owner
"mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar" \  
&& echo -e "\nconfluence.home=${CONF_HOME}" >>
"${CONF_INSTALL}/confluence/WEB-INF/classes/confluence-init.properties" \  
&& xmlstarlet ed --inplace \  
\--delete "Server/@debug" \  
\--delete "Server/Service/Connector/@debug" \  
\--delete "Server/Service/Connector/@minProcessors" \  
\--delete "Server/Service/Connector/@maxProcessors" \  
\--delete "Server/Service/Connector/@useURIValidationHack" \  
\--delete "Server/Service/Engine/@debug" \  
\--delete "Server/Service/Engine/Host/@debug" \  
\--delete "Server/Service/Engine/Host/Context/@debug" \  
"${CONF_INSTALL}/conf/server.xml" \  
&& sed -ri "s/-Xms1024m -Xmx1024m//" "${CONF_INSTALL}/bin/setenv.sh" \  
# && sed -ri 's~export CATALINA_OPTS~. ${CONF_INSTALL}/bin/set-remote-
debug.sh\nexport CATALINA_OPTS~' ${CONF_INSTALL}/bin/setenv.sh \  
&& mkdir -p "${CONF_INSTALL}/conf/Standalone" \  
&& chmod -R 777 "${CONF_INSTALL}" \  
&& chown -R ${RUN_USER}: "${CONF_INSTALL}" \  
&& mkdir "${IMPORTPATH}" \  
&& chown ${RUN_USER}: /usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts  
  
COPY newrelic-java-${NEWRELIC_VERSION}.zip ${CONF_INSTALL}/  
COPY configure-and-start-root.sh ${CONF_INSTALL}/bin/  
COPY configure-and-start.sh ${CONF_INSTALL}/bin/  
RUN chmod 500 ${CONF_INSTALL}/bin/configure-and-start*.sh \  
&& chown ${RUN_USER}: "${CONF_INSTALL}/bin/configure-and-start.sh" \  
&& chown ${RUN_USER}: "${CONF_INSTALL}/newrelic-java-${NEWRELIC_VERSION}.zip"  
  
# expose default ``Atlassian Confluence`` Remote Debug Target port  
EXPOSE 5005  
# expose default ``Atlassian Confluence`` HTTP port  
EXPOSE 8090  
# expose default ``Atlassian Confluence`` Synchrony port  
EXPOSE 8091  
# set volume mount points for installation and home directory  
VOLUME ["${CONF_HOME}"]  
  
# Set the default working directory as the installation directory.  
WORKDIR ${CONF_INSTALL}  
  
# Run Atlassian Confluence as a foreground process by default.  
ENTRYPOINT ["bin/configure-and-start-root.sh"]  

