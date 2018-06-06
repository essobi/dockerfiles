FROM hope/java:8  
  
MAINTAINER Sergey Sadovoi <sergey@hope.ua>  
  
ENV \  
CONF_VERSION=5.10.6 \  
CONF_PORT=8090 \  
CONF_INSTALL=/usr/local/confluence \  
MYSQL_CONNECTOR_VERSION=5.1.39  
  
RUN \  
apk add --no-cache --virtual=build-dependencies wget ca-certificates tar && \  
cd "/tmp" && \  
  
# Confluence install  
# https://www.atlassian.com/software/confluence/download  
wget https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONF_VERSION}.tar.gz && \  
mkdir -p ${CONF_INSTALL} && \  
tar -xzf atlassian-confluence-${CONF_VERSION}.tar.gz -C ${CONF_INSTALL}
\--strip-components=1 && \  
echo -e "\nconfluence.home=/data" >> "${CONF_INSTALL}/confluence/WEB-
INF/classes/confluence-init.properties" && \  
  
# MySQL connector  
# https://dev.mysql.com/downloads/connector/j/  
wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.tar.gz && \  
tar -xzf mysql-connector-java-${MYSQL_CONNECTOR_VERSION}.tar.gz && \  
mv mysql-connector-java-${MYSQL_CONNECTOR_VERSION}/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}-bin.jar ${CONF_INSTALL}/confluence/WEB-INF/lib
&& \  
  
# Cleanup  
apk del build-dependencies && \  
rm -rf "/tmp/"*  
  
VOLUME /data  
  
EXPOSE ${CONF_PORT}  
  
ENTRYPOINT ["/usr/local/confluence/bin/start-confluence.sh", "-fg"]  

