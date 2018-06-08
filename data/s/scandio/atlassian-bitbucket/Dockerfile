FROM ubuntu:latest  
MAINTAINER Scandio GmbH  
  
ENV BITBUCKET_HOME /var/atlassian/application-data/bitbucket  
ENV BITBUCKET_INSTALL /opt/atlassian/bitbucket  
ENV MYSQL_DRIVER_VERSION 5.1.36  
ENV BITBUCKET_VERSION 4.0.1  
ENV DOWNLOAD_URL
https://downloads.atlassian.com/software/stash/downloads/atlassian-
bitbucket-${BITBUCKET_VERSION}.tar.gz  
  
#ENV BITBUCKET_REMOTE_DEBUG false  
ENV RAM_MIN 512  
ENV RAM_MAX 2048  
#ENV DEBUG_PORT 5050  
#ENV HTTPS false  
#ENV PROXY_NAME false  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
ENV IMPORTCERT false  
ENV IMPORTPATH /var/certificates  
  
#ENV NEWRELIC_VERSION 3.17.0  
#ENV NEWRELIC_APP_NAME jira-docker  
#ENV NEWRELIC_LICENSE unknown  
#ENV WAIT false  
#ENV WAIT_COMMAND none  
#ENV WAIT_SLEEP 2  
#ENV WAIT_LOOPS 10  
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
ssh \  
wget \  
curl \  
unzip \  
&& \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
RUN mkdir -p ${BITBUCKET_INSTALL} \  
&& curl -L --silent ${DOWNLOAD_URL} | tar -xz --strip=1 -C
"$BITBUCKET_INSTALL" \  
&& mkdir -p ${BITBUCKET_INSTALL}/conf/Catalina \  
&& chmod -R 700 ${BITBUCKET_INSTALL}/conf/Catalina \  
&& chmod -R 700 ${BITBUCKET_INSTALL}/logs \  
&& chmod -R 700 ${BITBUCKET_INSTALL}/temp \  
&& chmod -R 700 ${BITBUCKET_INSTALL}/work \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BITBUCKET_INSTALL}/ \  
&& wget "http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& tar -xzf "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& mv "mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar" "${BITBUCKET_INSTALL}/lib/." \  
&& rm "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& rm -rf "mysql-connector-java-${MYSQL_DRIVER_VERSION}" \  
&& ln --symbolic "/usr/lib/x86_64-linux-gnu/libtcnative-1.so"
"${BITBUCKET_INSTALL}/lib/native/libtcnative-1.so" \  
&& chown -R ${RUN_USER} ${BITBUCKET_INSTALL}  
  
COPY configure-and-start.sh ${BITBUCKET_INSTALL}/bin/  
RUN chown ${RUN_USER}: ${BITBUCKET_INSTALL}/bin/configure-and-start.sh  
RUN mkdir ${IMPORTPATH}  
RUN chown ${RUN_USER}: /usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts  
  
USER ${RUN_USER}  
  
# HTTP Port  
EXPOSE 7990  
# SSH Port  
EXPOSE 7999  
VOLUME ["${BITBUCKET_HOME}"]  
  
WORKDIR $BITBUCKET_INSTALL  
  
# Run in foreground  
CMD ["./bin/configure-and-start.sh"]  

