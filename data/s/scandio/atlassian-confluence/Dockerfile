FROM ubuntu:latest  
MAINTAINER Philipp Goellner <philipp@goellner.it>, Philipp Goellner
<philipp.goellner@scandio.de>  
  
# setup useful environment variables  
ENV CONF_HOME /var/atlassian/confluence  
ENV CONF_INSTALL /opt/atlassian/confluence  
ENV MYSQL_DRIVER_VERSION 5.1.36  
ENV CONF_VERSION 5.8.14  
ENV DOWNLOAD_URL
http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONF_VERSION}.tar.gz  
  
ENV CONF_REMOTE_DEBUG false  
ENV RAM_MIN 1024  
ENV RAM_MAX 2048  
ENV DEBUG_PORT 5005  
ENV HTTPS false  
ENV IMPORTCERT false  
ENV IMPORTPATH /var/certificates  
  
ENV PROXY_NAME false  
  
ENV RUN_USER daemon  
  
ENV NEWRELIC_VERSION 3.19.0  
ENV NEWRELIC_APP_NAME confluence-docker  
ENV NEWRELIC_LICENSE unknown  
  
ENV WAIT false  
ENV WAIT_COMMAND none  
ENV WAIT_SLEEP 2  
ENV WAIT_LOOPS 10  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886
&& \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu/ precise main" >
/etc/apt/sources.list.d/java.list && \  
echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-set-
selections && \  
echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-set-
selections && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean && \  
echo -n > /var/lib/apt/extended_states \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends libtcnative-1
xmlstarlet ssh wget curl sed unzip \  
&& apt-get clean \  
&& mkdir -p "${CONF_HOME}" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} "${CONF_HOME}" \  
&& mkdir -p "${CONF_INSTALL}" \  
&& curl -Ls ${DOWNLOAD_URL} | tar -xz --directory "${CONF_INSTALL}/" \--strip-
components=1 \  
&& chmod -R 777 "${CONF_INSTALL}/temp" \  
&& chmod -R 777 "${CONF_INSTALL}/logs" \  
&& chmod -R 777 "${CONF_INSTALL}/work" \  
&& mkdir -p "${CONF_INSTALL}/conf/Standalone" \  
&& chmod -R 777 "${CONF_INSTALL}/conf/Standalone" \  
&& echo -e "\nconfluence.home=$CONF_HOME" >> "${CONF_INSTALL}/confluence/WEB-
INF/classes/confluence-init.properties" \  
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
&& wget "http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& tar -xzf "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& mv "mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar" "${CONF_INSTALL}/lib/." \  
&& rm "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& rm -rf "mysql-connector-java-${MYSQL_DRIVER_VERSION}" \  
&& sed -ri "s/-Xms1024m -Xmx1024m//" ${CONF_INSTALL}/bin/setenv.sh \  
# && sed -ri 's~export CATALINA_OPTS~. ${CONF_INSTALL}/bin/set-remote-
debug.sh\nexport CATALINA_OPTS~' ${CONF_INSTALL}/bin/setenv.sh \  
&& chown -R ${RUN_USER}: "${CONF_INSTALL}"  
COPY configure-and-start.sh ${CONF_INSTALL}/bin/  
RUN chown ${RUN_USER}: ${CONF_INSTALL}/bin/configure-and-start.sh  
COPY newrelic-java-${NEWRELIC_VERSION}.zip ${CONF_INSTALL}/  
RUN chown ${RUN_USER}: ${CONF_INSTALL}/newrelic-java-${NEWRELIC_VERSION}.zip  
RUN mkdir ${IMPORTPATH}  
RUN chown ${RUN_USER}: /usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts  
  
# run ``Atlassian Confluence`` as unprivileged user by default  
USER ${RUN_USER}  
  
# expose default ``Atlassian Confluence`` HTTP port  
EXPOSE 8090 5005  
# set volume mount points for installation and home directory  
VOLUME ["${CONF_HOME}"]  
  
# Set the default working directory as the installation directory.  
WORKDIR ${CONF_INSTALL}  
  
# Run Atlassian Confluence as a foreground process by default.  
CMD ["bin/configure-and-start.sh"]  

