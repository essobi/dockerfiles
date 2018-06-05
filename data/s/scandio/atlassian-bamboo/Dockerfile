FROM ubuntu:latest  
MAINTAINER Göllner IT info@goellner-it.de  
  
ENV MYSQL_DRIVER_VERSION 5.1.36  
ENV BAMBOO_VERSION 5.10.1.1  
ENV DOWNLOAD_URL
https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-bamboo-  
  
ENV BAMBOO_HOME /var/atlassian/application-data/bamboo  
  
ENV BAMBOO_INSTALL /opt/atlassian/bamboo  
  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
ENV BAMBOO_REMOTE_DEBUG false  
ENV RAM_MIN 1024  
ENV RAM_MAX 2048  
ENV DEBUG_PORT 5005  
ENV HTTPS false  
ENV IMPORTCERT false  
ENV IMPORTPATH /var/certificates  
  
ENV BACKUP_HOST false  
ENV BACKUP_PATH false  
ENV BACKUP_USER false  
ENV BACKUP_SSHKEY false  
  
ENV PROXY_NAME false  
  
ENV NEWRELIC_VERSION 3.19.0  
ENV NEWRELIC_APP_NAME confluence-docker  
ENV NEWRELIC_LICENSE unknown  
  
ENV WAIT false  
ENV WAIT_COMMAND none  
ENV WAIT_SLEEP 2  
ENV WAIT_LOOPS 10  
# Install Java, git, other dependencies, download and extract Bamboo and
create the required directory layout.  
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
apt-get install -y --no-install-recommends \  
git \  
libtcnative-1 \  
xmlstarlet \  
xmlstarlet \  
openssh-client \  
wget \  
curl \  
unzip \  
rsync \  
&& \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
RUN mkdir -p ${BAMBOO_INSTALL}  
  
RUN curl -L --silent ${DOWNLOAD_URL}${BAMBOO_VERSION}.tar.gz | tar -xz
--strip=1 -C "${BAMBOO_INSTALL}" \  
&& mkdir -p ${BAMBOO_INSTALL}/conf/Catalina \  
&& chmod -R 700 ${BAMBOO_INSTALL}/conf/Catalina \  
&& chmod -R 700 ${BAMBOO_INSTALL}/logs \  
&& chmod -R 700 ${BAMBOO_INSTALL}/temp \  
&& chmod -R 700 ${BAMBOO_INSTALL}/work \  
&& wget "http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& tar -xzf "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& mv "mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar" "${BAMBOO_INSTALL}/lib/." \  
&& chown -R ${RUN_USER}: ${BAMBOO_INSTALL}  
  
ADD bamboo-init.properties ${BAMBOO_INSTALL}/atlassian-bamboo/WEB-INF/classes/  
  
#RUN wget "http://dl.bintray.com/jfrog/jfrog-jars/org/jfrog/bamboo/bamboo-
artifactory-plugin/1.8.2/bamboo-artifactory-plugin-1.8.2.jar" \  
# && mv bamboo-artifactory-plugin-1.8.2.jar ${BAMBOO_INSTALL}/atlassian-
bamboo/WEB-INF/lib/  
COPY configure-and-start.sh ${BAMBOO_INSTALL}/bin/  
RUN chown ${RUN_USER}: ${BAMBOO_INSTALL}/bin/configure-and-start.sh  
RUN mkdir ${IMPORTPATH}  
RUN chown ${RUN_USER}: /usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts  
  
USER ${RUN_USER}  
  
VOLUME ["${BAMBOO_HOME}"]  
  
# HTTP Port  
EXPOSE 8085  
WORKDIR $BAMBOO_INSTALL  
  
# Run in foreground  
CMD ["./bin/configure-and-start.sh"]  

