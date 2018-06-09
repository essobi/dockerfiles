FROM exira/java:8.92.14-r1  
  
MAINTAINER exira.com <info@exira.com>  
  
ARG CONTAINER_UID=1003  
ARG CONTAINER_GID=1003  
# https://download.jetbrains.com/teamcity/TeamCity-10.0.1.tar.gz  
ENV TEAMCITY_VERSION=10.0.1 \  
TEAMCITY_DATA_PATH=/var/lib/teamcity \  
TEAMCITY_INSTALL_PATH=/opt \  
MYSQL_DRIVER_VERSION=5.1.38 \  
# 9.3-1103.jdbc4, 9.3-1104.jdbc4, 9.4-1202.jdbc4, 9.4-1202.jdbc4,
9.4-1203.jdbc4, 9.4-1204.jdbc4, 9.4-1205.jdbc4, 9.4-1206-jdbc4, 9.4.1207.jre6,
9.4.1208.jre6  
POSTGRESQL_VERSION=9.4.1208.jre6 \  
# 4.0.2206.100, 4.1.5605.100, 4.2.6420.100  
MSSQL_DRIVER_VERSION=4.1.5605.100 \  
MSSQL_DRIVER_MAIN_VERSION=4.1 \  
CONTAINER_USER=teamcity \  
CONTAINER_GROUP=teamcity  
  
RUN \  
# fix wget https  
build_pkgs="wget ca-certificates" && \  
apk update && \  
apk upgrade && \  
apk --update --no-cache add ${build_pkgs} && \  
update-ca-certificates && \  
  
# install teamcity  
mkdir -p ${TEAMCITY_INSTALL_PATH} && \  
wget -O /tmp/TeamCity-${TEAMCITY_VERSION}.tar.gz
https://download.jetbrains.com/teamcity/TeamCity-${TEAMCITY_VERSION}.tar.gz &&
\  
tar xzf /tmp/TeamCity-${TEAMCITY_VERSION}.tar.gz -C ${TEAMCITY_INSTALL_PATH}
&& \  
rm -rf ${TEAMCITY_INSTALL_PATH}/buildAgent && \  
  
# configure teamcity  
sed -i -e "s/\\.*<\/Host>.*$/<Valve
className=\"org.apache.catalina.valves.RemoteIpValve\"
protocolHeader=\"x-forwarded-proto\" \/><\/Host>/"
${TEAMCITY_INSTALL_PATH}/TeamCity/conf/server.xml && \  
mkdir -p ${TEAMCITY_DATA_PATH}/lib/jdbc && \  
# install mysql drivers  
rm -f ${TEAMCITY_DATA_PATH}/lib/jdbc/mysql-connector-java*.jar && \  
wget -O /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz
http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz && \  
tar xzf /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz -C /tmp && \  
cp /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar ${TEAMCITY_DATA_PATH}/lib/jdbc/mysql-
connector-java-${MYSQL_DRIVER_VERSION}-bin.jar && \  
# install postgresl drivers  
rm -f ${TEAMCITY_DATA_PATH}/lib/jdbc/postgresql*.jar && \  
wget -O ${TEAMCITY_DATA_PATH}/lib/jdbc/postgresql-${POSTGRESQL_VERSION}.jar
http://jdbc.postgresql.org/download/postgresql-${POSTGRESQL_VERSION}.jar && \  
# install mssql drivers  
rm -f ${TEAMCITY_DATA_PATH}/lib/jdbc/sqljdbc*.jar && \  
wget -O /tmp/sqljdbc_${MSSQL_DRIVER_VERSION}_enu.tar.gz
https://download.microsoft.com/download/0/2/A/02AAE597-3865-456C-AE7F-613F99F850A8/sqljdbc_${MSSQL_DRIVER_VERSION}_enu.tar.gz
&& \  
gzip -d /tmp/sqljdbc_${MSSQL_DRIVER_VERSION}_enu.tar.gz && \  
tar xf /tmp/sqljdbc_${MSSQL_DRIVER_VERSION}_enu.tar -C /tmp && \  
cp /tmp/sqljdbc_${MSSQL_DRIVER_MAIN_VERSION}/enu/sqljdbc4.jar
${TEAMCITY_DATA_PATH}/lib/jdbc/sqljdbc4.jar && \  
# add teamcity user  
mkdir -p /home/${CONTAINER_USER} && \  
addgroup -g $CONTAINER_GID -S ${CONTAINER_GROUP} && \  
adduser -u $CONTAINER_UID -S -D -G ${CONTAINER_GROUP} -h
/home/${CONTAINER_USER} -s /bin/sh ${CONTAINER_USER} && \  
chown -R ${CONTAINER_USER}:${CONTAINER_GROUP} /home/${CONTAINER_USER} && \  
chown -R ${CONTAINER_USER}:${CONTAINER_GROUP} ${TEAMCITY_INSTALL_PATH} && \  
chown -R ${CONTAINER_USER}:${CONTAINER_GROUP} ${TEAMCITY_DATA_PATH} && \  
  
# remove dev dependencies  
apk del ${build_pkgs} && \  
  
# other clean up  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/* && \  
rm -rf /var/log/*  
  
# Prefer ipv4, comment if you want to bind to ipv6  
ENV CATALINA_OPTS="-Djava.net.preferIPv4Stack=true"  
# Expose default HTTP connector port.  
EXPOSE 8111  
# Set volume mount points for data directory  
VOLUME ${TEAMCITY_DATA_PATH}  
  
CMD ["su", "-m", "teamcity", "-c", "/opt/TeamCity/bin/teamcity-server.sh run"]  
#CMD ["/opt/TeamCity/bin/teamcity-server.sh run"]  

