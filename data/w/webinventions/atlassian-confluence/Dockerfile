FROM debian:stretch  
  
# Update system and install required packages  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq \  
&& apt-get install -y wget curl git unzip libtcnative-1 xmlstarlet gosu \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
# Oracle JDK  
ENV ORACLE_JDK_VERSION jdk-8u172  
ENV ORACLE_JDK_URL http://download.oracle.com/otn-
pub/java/jdk/8u172-b11/a58eab1ec242421181065cdc37240b08/jdk-8u172-linux-x64.tar.gz  
RUN mkdir -p /opt/jdk/$ORACLE_JDK_VERSION && \  
wget --header "Cookie: oraclelicense=accept-securebackup-cookie" -O
/opt/jdk/$ORACLE_JDK_VERSION/$ORACLE_JDK_VERSION.tar.gz $ORACLE_JDK_URL && \  
tar -zxf /opt/jdk/$ORACLE_JDK_VERSION/$ORACLE_JDK_VERSION.tar.gz --strip-
components=1 -C /opt/jdk/$ORACLE_JDK_VERSION && \  
rm /opt/jdk/$ORACLE_JDK_VERSION/$ORACLE_JDK_VERSION.tar.gz && \  
update-alternatives --install /usr/bin/java java
/opt/jdk/$ORACLE_JDK_VERSION/bin/java 100 && \  
update-alternatives --install /usr/bin/javac javac
/opt/jdk/$ORACLE_JDK_VERSION/bin/javac 100  
  
ENV JAVA_HOME /opt/jdk/${ORACLE_JDK_VERSION}  
ENV JAVA_TRUSTSTORE ${JAVA_HOME}/jre/lib/security/cacerts  
ENV JAVA_TRUSTSTORE_PASSWORD changeit  
  
ENV CATALINA_OPTS "-Djavax.net.ssl.trustStore=${JAVA_TRUSTSTORE}
-Djavax.net.ssl.trustStorePassword=${JAVA_TRUSTSTORE_PASSWORD}"  
ENV RUN_USER atlassian  
ENV RUN_USER_UID 5000  
ENV RUN_GROUP atlassian  
ENV RUN_GROUP_GID 5000  
RUN \  
groupadd --gid ${RUN_GROUP_GID} -r ${RUN_GROUP} && \  
useradd -r --uid ${RUN_USER_UID} -g ${RUN_GROUP} ${RUN_USER}  
  
ENV CONFLUENCE_VERSION 6.9.0  
ENV CONFLUENCE_HOME /var/atlassian/confluence/data  
ENV CONFLUENCE_INSTALL_DIR /opt/atlassian/confluence  
ENV DOWNLOAD_URL
https://downloads.atlassian.com/software/confluence/downloads/atlassian-
confluence-  
  
RUN mkdir -p ${CONFLUENCE_HOME} ${CONFLUENCE_INSTALL_DIR} && \  
curl -L --silent ${DOWNLOAD_URL}${CONFLUENCE_VERSION}.tar.gz | tar -xz
--strip=1 -C "$CONFLUENCE_INSTALL_DIR" && \  
chown -R ${RUN_USER}:${RUN_GROUP} ${CONFLUENCE_HOME} ${CONFLUENCE_INSTALL_DIR}  
  
# MySQL connector  
ENV MYSQL_CONNECTOR_VERSION 5.1.44  
RUN \  
wget -O ${CONFLUENCE_INSTALL_DIR}/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.tar.gz
http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.tar.gz && \  
tar xzf ${CONFLUENCE_INSTALL_DIR}/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.tar.gz -C ${CONFLUENCE_INSTALL_DIR} && \  
mv ${CONFLUENCE_INSTALL_DIR}/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}-bin.jar ${CONFLUENCE_INSTALL_DIR}/lib/ && \  
rm -rf ${CONFLUENCE_INSTALL_DIR}/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.tar.gz ${CONFLUENCE_INSTALL_DIR}/mysql-
connector-java-${MYSQL_CONNECTOR_VERSION}  
  
# Confluence home dir  
RUN echo "confluence.home=${CONFLUENCE_HOME}" >
${CONFLUENCE_INSTALL_DIR}/confluence/WEB-INF/classes/confluence-
init.properties  
  
ENV PATH $CONFLUENCE_INSTALL_DIR/bin:$JAVA_HOME/bin:$PATH  
  
# HTTP Port  
EXPOSE 8090  
COPY docker-entrypoint.sh /entrypoint.sh  
  
RUN chmod a+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
WORKDIR $CONFLUENCE_INSTALL_DIR  
  
# Run in foreground  
CMD ["start-confluence.sh", "-fg"]

