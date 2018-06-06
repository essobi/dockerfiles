FROM exira/java:latest  
  
MAINTAINER exira.com <info@exira.com>  
  
ARG CONTAINER_UID=1000  
ARG CONTAINER_GID=1000  
  
ENV CONFLUENCE_VERSION=5.9.7 \  
CONF_HOME=/var/atlassian/confluence \  
CONF_INSTALL=/opt/atlassian/confluence \  
CONFLUENCE_CATALINA_TMPDIR=/var/atlassian/confluence/temp \  
MYSQL_DRIVER_VERSION=5.1.38 \  
CONTAINER_USER=confluence \  
CONTAINER_GROUP=confluence  
  
RUN \  
# Install build and runtime packages  
build_pkgs="gzip tar wget" && \  
apk update && \  
apk upgrade && \  
apk --update --no-cache add ${build_pkgs} && \  
  
# add confluence user  
mkdir -p /home/${CONTAINER_USER} && \  
addgroup -g $CONTAINER_GID -S ${CONTAINER_GROUP} && \  
adduser -u $CONTAINER_UID -S -D -G ${CONTAINER_GROUP} -h
/home/${CONTAINER_USER} -s /bin/sh ${CONTAINER_USER} && \  
chown -R ${CONTAINER_USER}:${CONTAINER_GROUP} /home/${CONTAINER_USER} && \  
  
# create confluence structure  
mkdir -p ${CONF_HOME} && \  
mkdir -p ${CONFLUENCE_CATALINA_TMPDIR} && \  
chown -R ${CONTAINER_USER}:${CONTAINER_GROUP} ${CONF_HOME} && \  
mkdir -p ${CONF_INSTALL}/conf && \  
  
# install confluence  
wget -O /tmp/atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz
http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONFLUENCE_VERSION}.tar.gz && \  
tar xzf /tmp/atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz --strip-
components=1 -C ${CONF_INSTALL} && \  
echo "confluence.home=${CONF_HOME}" > ${CONF_INSTALL}/confluence/WEB-
INF/classes/confluence-init.properties && \  
  
# Install database drivers  
rm -f ${CONF_INSTALL}/lib/mysql-connector-java*.jar && \  
wget -O /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz
http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz && \  
tar xzf /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz -C /tmp && \  
cp /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar ${CONF_INSTALL}/lib/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar && \  
chown -R ${CONTAINER_USER}:${CONTAINER_GROUP} ${CONF_INSTALL} && \  
  
# remove dev dependencies  
apk del ${build_pkgs} && \  
  
# other clean up  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/* && \  
rm -rf /var/log/*  
  
# Prefer ipv4, comment if you want to bind to ipv6  
ENV CATALINA_OPTS="-Djava.net.preferIPv4Stack=true"  
# Expose default HTTP connector port.  
EXPOSE 8090  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs.  
VOLUME ["/var/atlassian/confluence"]  
  
# Set the default working directory as the Confluence home directory.  
WORKDIR ${CONF_HOME}  
  
CMD ["su", "-m", "confluence", "-c",
"/opt/atlassian/confluence/bin/catalina.sh run"]  
  

