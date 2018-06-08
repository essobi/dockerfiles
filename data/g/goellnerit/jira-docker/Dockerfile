FROM ubuntu:latest  
MAINTAINER Philipp Goellner, philipp.goellner@xaltbc.de  
  
# setup useful environment variables  
ENV TIME_ZONE Europe/Berlin  
  
ENV JIRA_HOME /var/atlassian/jira  
ENV JIRA_INSTALL /opt/atlassian/jira  
ENV MYSQL_DRIVER_VERSION 5.1.36  
ENV JIRA_VERSION 7.4.2  
ENV DOWNLOAD_URL
https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-
software-${JIRA_VERSION}.tar.gz  
  
ENV JIRA_REMOTE_DEBUG false  
ENV RAM_MIN 512m  
ENV RAM_MAX 2048m  
ENV HTTPS false  
ENV IMPORTCERT false  
ENV IMPORTPATH /var/certificates  
  
ENV PROXY_NAME false  
  
ENV RUN_USER daemon  
  
ENV NEWRELIC_VERSION 3.36.0  
ENV NEWRELIC_APP_NAME jira-docker  
ENV NEWRELIC_LICENSE unknown  
  
ENV INSTALL_PLUGINS false  
ENV INSTALL_PLUGINS_URLS_V1 false  
ENV INSTALL_PLUGINS_URLS_V2 false  
  
ENV WAIT false  
ENV WAIT_COMMAND none  
ENV WAIT_SLEEP 2  
ENV WAIT_LOOPS 10  
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
&& apt-get update \  
&& apt-get install -y oracle-java8-installer \  
rsync \  
openssh-client \  
&& apt-get clean \  
&& echo -n > /var/lib/apt/extended_states \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends libtcnative-1
xmlstarlet wget curl sed unzip \  
&& apt-get clean \  
&& mkdir -p "${JIRA_HOME}" \  
&& mkdir -p "${JIRA_INSTALL}" \  
&& curl -Ls ${DOWNLOAD_URL} | tar -xz --directory "${JIRA_INSTALL}/" \--strip-
components=1 \  
&& wget "http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& tar -xzf "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& mv "mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar" "${JIRA_INSTALL}/lib/." \  
&& rm "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& rm -rf "mysql-connector-java-${MYSQL_DRIVER_VERSION}" \  
&& sed -ri "s/-Xms${JVM_MINIMUM_MEMORY} -Xmx${JVM_MAXIMUM_MEMORY}//"
${JIRA_INSTALL}/bin/setenv.sh \  
&& chown -R ${RUN_USER}: "${JIRA_INSTALL}" "${JIRA_HOME}" \  
&& echo "jira.home = ${JIRA_HOME}" > ${JIRA_INSTALL}/atlassian-jira/WEB-
INF/classes/jira-application.properties  
  
COPY setenv.sh ${JIRA_INSTALL}/bin/  
COPY newrelic-java-${NEWRELIC_VERSION}.zip ${JIRA_INSTALL}/  
COPY configure-and-start-root.sh ${JIRA_INSTALL}/bin/  
COPY configure-and-start.sh ${JIRA_INSTALL}/bin/  
RUN chmod 500 ${JIRA_INSTALL}/bin/configure-and-start*.sh \  
&& chown ${RUN_USER}: ${JIRA_INSTALL}/bin/configure-and-start.sh \  
&& chown ${RUN_USER}: ${JIRA_INSTALL}/newrelic-java-${NEWRELIC_VERSION}.zip \  
&& mkdir ${IMPORTPATH} \  
&& chown ${RUN_USER}: /usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts  
  
# set system time  
RUN apt-get install -qy tzdata \  
&& cp -f /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime \  
&& echo ${TIME_ZONE} > /etc/timezone  
  
# expose default ``Atlassian JIRA`` HTTP port  
EXPOSE 8080 5005  
# set volume mount points for installation and home directory  
VOLUME ["${JIRA_HOME}"]  
  
# Set the default working directory as the installation directory.  
WORKDIR ${JIRA_INSTALL}  
  
# Run Atlassian JIRA as a foreground process by default.  
ENTRYPOINT ["bin/configure-and-start-root.sh", "-fg"]  

