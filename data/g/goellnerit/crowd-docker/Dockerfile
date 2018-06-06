FROM ubuntu:latest  
MAINTAINER Philipp Goellner <philipp@goellner.it>, Philipp Goellner
<philipp.goellner@xaltbc.de>  
  
# setup useful environment variables  
ENV CROWD_HOME /var/atlassian/crowd  
ENV CROWD_INSTALL /opt/atlassian/crowd  
ENV MYSQL_DRIVER_VERSION 5.1.36  
ENV CROWD_VERSION 2.8.8  
ENV DOWNLOAD_URL
https://www.atlassian.com/software/crowd/downloads/binary/atlassian-
crowd-${CROWD_VERSION}.tar.gz  
  
#TODO  
#ENV CROWD_REMOTE_DEBUG false  
ENV RAM_MIN 768  
ENV RAM_MAX 2048  
#TODO  
#ENV DEBUG_PORT 5005  
ENV HTTPS false  
ENV IMPORTCERT false  
ENV IMPORTPATH /var/certificates  
  
ENV BACKUP_HOST false  
ENV BACKUP_PATH false  
ENV BACKUP_USER false  
ENV BACKUP_KEY_FILE /tmp/id_rsa  
  
ENV PROXY_NAME false  
  
ENV RUN_USER daemon  
  
ENV NEWRELIC_VERSION 3.19.0  
ENV NEWRELIC_APP_NAME crowd-docker  
ENV NEWRELIC_LICENSE unknown  
  
ENV WAIT false  
ENV WAIT_COMMAND none  
ENV WAIT_SLEEP 2  
ENV WAIT_LOOPS 10  
ENV CROWD_URL https://crowd.scandio  
ENV CROWD_CONTEXT ROOT  
ENV CROWDDB_URL mysql://dbuser:dbpass@dbhost:dbport/dbname  
ENV CROWDID_CONTEXT ""  
ENV DEMO_CONTEXT demo  
  
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
xmlstarlet openssh-client wget curl sed unzip rsync \  
&& apt-get clean \  
&& mkdir -p "${CROWD_HOME}" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} "${CROWD_HOME}" \  
&& mkdir -p "${CROWD_INSTALL}" \  
&& curl -Ls ${DOWNLOAD_URL} | tar -xz --directory "${CROWD_INSTALL}/"
\--strip-components=1 \  
&& echo "\ncrowd.home=$CROWD_HOME" >> "${CROWD_INSTALL}/crowd-webapp/WEB-
INF/classes/crowd-init.properties" \  
&& sed -i 's|exec "$PRGDIR"\/"$EXECUTABLE" start "$@"|exec
"$PRGDIR"/"$EXECUTABLE" run "$@"|g' ${CROWD_INSTALL}/apache-
tomcat/bin/startup.sh \  
#TODO  
# && xmlstarlet ed --inplace \  
# --delete "Server/@debug" \  
# --delete "Server/Service/Connector/@debug" \  
# --delete "Server/Service/Connector/@minProcessors" \  
# --delete "Server/Service/Connector/@maxProcessors" \  
# --delete "Server/Service/Connector/@useURIValidationHack" \  
# --delete "Server/Service/Engine/@debug" \  
# --delete "Server/Service/Engine/Host/@debug" \  
# --delete "Server/Service/Engine/Host/Context/@debug" \  
# "${CROWD_INSTALL}/conf/server.xml" \  
&& mv ${CROWD_INSTALL}/apache-tomcat/webapps/ROOT ${CROWD_INSTALL}/splash-
webapp \  
&& mv ${CROWD_INSTALL}/apache-tomcat/conf/Catalina/localhost
${CROWD_INSTALL}/webapps \  
&& mkdir ${CROWD_INSTALL}/apache-tomcat/conf/Catalina/localhost \  
&& wget "http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& tar -xzf "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& mv "mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar" "${CROWD_INSTALL}/apache-tomcat/lib/." \  
&& rm "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& rm -rf "mysql-connector-java-${MYSQL_DRIVER_VERSION}" \  
#TODO  
# && sed -ri "s/-Xms1024m -Xmx1024m//" ${CROWD_INSTALL}/bin/setenv.sh \  
## && sed -ri 's~export CATALINA_OPTS~. ${CROWD_INSTALL}/bin/set-remote-
debug.sh\nexport CATALINA_OPTS~' ${CROWD_INSTALL}/bin/setenv.sh \  
# && chown -R ${RUN_USER}: "${CROWD_INSTALL}"  
ADD splash-context.xml ${CROWD_INSTALL}/webapps/splash.xml  
  
COPY common.bash ${CROWD_INSTALL}/  
COPY configure-and-start.sh ${CROWD_INSTALL}/  
COPY newrelic-java-${NEWRELIC_VERSION}.zip ${CROWD_INSTALL}/  
  
RUN chown -R ${RUN_USER}: ${CROWD_INSTALL}  
RUN mkdir ${IMPORTPATH}  
RUN chown ${RUN_USER}: /usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts  
  
# run ``Atlassian Crowd`` as unprivileged user by default  
USER ${RUN_USER}  
  
# expose default ``Atlassian Crowd`` HTTP port  
EXPOSE 8095 5005  
# set volume mount points for installation and home directory  
VOLUME ["${CROWD_HOME}", "${IMPORTPATH}"]  
  
# Set the default working directory as the installation directory.  
WORKDIR ${CROWD_INSTALL}  
  
# Run Atlassian Crowd as a foreground process by default.  
CMD ["./configure-and-start.sh"]

