#  
# BUILD : DF/[ATLASSIAN][BITBUCKET]  
# OS/CORE : java:8  
# SERVICES : -  
#  
# VERSION 1.0.2  
#  
FROM java:8  
MAINTAINER Patrick Paechnatz <patrick.paechnatz@gmail.com>  
LABEL com.container.vendor="dunkelfrosch impersonate" \  
com.container.service="atlassian/bitbucket" \  
com.container.service.version="5.1.3" \  
com.container.priority="1" \  
com.container.project="bitbucket" \  
img.version="1.0.2" \  
img.description="atlassian bitbucket application container"  
  
ENV TERM="xterm" \  
LC_ALL="C.UTF-8" \  
DEBIAN_FRONTEND="noninteractive" \  
TIMEZONE="Europe/Berlin" \  
BITBUCKET_VERSION="5.1.3" \  
BITBUCKET_HOME="/var/atlassian/application-data/bitbucket" \  
BITBUCKET_INSTALL_DIR="/opt/atlassian/bitbucket" \  
DOWNLOAD_URL="https://downloads.atlassian.com/software/stash/downloads/atlassian-
bitbucket-" \  
JVM_MYSQL_CONNECTOR_URL="http://dev.mysql.com/get/Downloads/Connector-J" \  
JVM_MYSQL_CONNETOR="mysql-connector-java-5.1.36" \  
JAVA_HOME="/usr/lib/jvm/java-1.8.0-openjdk-amd64" \  
RUN_USER="daemon" \  
RUN_GROUP="daemon"  
# x-layer 1: package manager related processor  
RUN apt-get update -qq \  
&& apt-get install -qq -y --no-install-recommends software-properties-common
debconf-utils git liblucene2-java mc xmlstarlet ntp \  
&& apt-get clean autoclean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/cache /var/lib/log /tmp/* /var/tmp/*  
  
# x-layer 2: application base setup related processor  
RUN set -e \  
&& mkdir -p ${BITBUCKET_HOME}/lib \  
${BITBUCKET_INSTALL_DIR} \  
${BITBUCKET_INSTALL_DIR}/conf/Catalina \  
${BITBUCKET_INSTALL_DIR}/lib \  
&& curl -Ls "${DOWNLOAD_URL}${BITBUCKET_VERSION}.tar.gz" | tar -xz --strip=1
-C "${BITBUCKET_INSTALL_DIR}" \  
&& curl -Ls "${JVM_MYSQL_CONNECTOR_URL}/${JVM_MYSQL_CONNETOR}.tar.gz" | tar
-xz --directory "${BITBUCKET_INSTALL_DIR}/atlassian-bitbucket/WEB-INF/lib"
\--strip=1 --no-same-owner
"${JVM_MYSQL_CONNETOR}/${JVM_MYSQL_CONNETOR}-bin.jar" \  
&& chmod -R 700 ${BITBUCKET_HOME} ${BITBUCKET_INSTALL_DIR} \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BITBUCKET_HOME}
${BITBUCKET_INSTALL_DIR} \  
&& sed --in-place "s/# umask 0027/umask 0027/g"
"${BITBUCKET_INSTALL_DIR}/bin/setenv.sh" \  
&& sed -ie 's/\\(UMASK\s.\\)\\(0027\\)/\1 0027/g' /etc/login.defs  
  
# x-layer 3: application advanced setup related processor  
RUN set -e \  
&& echo "${TIMEZONE}" >/etc/timezone \  
&& dpkg-reconfigure tzdata >/dev/null 2>&1  
  
#  
# -> if you're running this bitbucket container outside a workbench scenario,
you  
# can activate VOLUME feature ...  
#  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory (accessing logs). These directories will be set-and-used during  
# data-only container volume bound run-mode.  
# VOLUME ["${BITBUCKET_INSTALL_DIR}", "${BITBUCKET_HOME}"]  
# Set application base communication port(s), bitbucket HTTP and bitbucket SSH  
EXPOSE 7990 7999  
# Next, set the default working directory as bitbucket home directory.  
WORKDIR ${BITBUCKET_INSTALL_DIR}  
  
# Set base container execution user/group (no root-right container allowed
here)  
# using the default unprivileged account.  
USER ${RUN_USER}:${RUN_GROUP}  
  
# Set entrypoint script for application, bitbucket will run as foreground
process (-fg)  
CMD ["./bin/start-bitbucket.sh", "-fg"]

