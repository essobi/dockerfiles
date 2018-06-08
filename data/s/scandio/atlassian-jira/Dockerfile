FROM ubuntu:latest  
MAINTAINER Philipp Goellner <philipp.goellner@scandio.de>  
  
# setup useful environment variables  
ENV JIRA_HOME /var/atlassian/jira  
ENV JIRA_INSTALL /opt/atlassian/jira  
ENV MYSQL_DRIVER_VERSION 5.1.36  
ENV JIRA_VERSION 6.4.12  
ENV DOWNLOAD_URL
http://www.atlassian.com/software/jira/downloads/binary/atlassian-
jira-${JIRA_VERSION}.tar.gz  
  
ENV JIRA_REMOTE_DEBUG false  
ENV RAM_MIN 512  
ENV RAM_MAX 2048  
ENV DEBUG_PORT 5050  
ENV HTTPS false  
ENV IMPORTCERT false  
ENV IMPORTPATH /var/certificates  
  
ENV PROXY_NAME false  
  
ENV RUN_USER daemon  
  
ENV NEWRELIC_VERSION 3.17.0  
ENV NEWRELIC_APP_NAME jira-docker  
ENV NEWRELIC_LICENSE unknown  
  
ENV INSTALL_PLUGINS false  
ENV INSTALL_PLUGINS_URLS_V1 false  
ENV INSTALL_PLUGINS_URLS_V2 false  
  
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
&& sed -ri "s/-Xms1024m -Xmx1024m//" ${JIRA_INSTALL}/bin/setenv.sh \  
&& chown -R ${RUN_USER}: "${JIRA_INSTALL}" "${JIRA_HOME}"  
RUN echo "jira.home = ${JIRA_HOME}" > ${JIRA_INSTALL}/atlassian-jira/WEB-
INF/classes/jira-application.properties  
  
COPY configure-and-start.sh ${JIRA_INSTALL}/bin/  
RUN chown ${RUN_USER}: ${JIRA_INSTALL}/bin/configure-and-start.sh  
COPY newrelic-java-${NEWRELIC_VERSION}.zip ${JIRA_INSTALL}/  
RUN chown ${RUN_USER}: ${JIRA_INSTALL}/newrelic-java-${NEWRELIC_VERSION}.zip  
RUN mkdir ${IMPORTPATH}  
RUN chown ${RUN_USER}: /usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts  
  
# run ``Atlassian JIRA`` as unprivileged user by default  
USER ${RUN_USER}  
  
# expose default ``Atlassian JIRA`` HTTP port  
EXPOSE 8080 5005  
# set volume mount points for installation and home directory  
VOLUME ["${JIRA_HOME}"]  
  
# Set the default working directory as the installation directory.  
WORKDIR ${JIRA_INSTALL}  
  
# Run Atlassian JIRA as a foreground process by default.  
CMD ["bin/configure-and-start.sh", "-fg"]  

