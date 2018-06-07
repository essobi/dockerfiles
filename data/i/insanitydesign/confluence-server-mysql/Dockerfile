FROM atlassian/confluence-server  
MAINTAINER INsanityDesign  
  
ENV MYSQL_DRIVER_VERSION 5.1.46  
RUN cd /tmp && wget "https://dev.mysql.com/get/Downloads/Connector-J/mysql-
connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& tar -xzf "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& mv "mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.jar" "${CONFLUENCE_INSTALL_DIR}/confluence/WEB-
INF/lib/." \  
&& rm "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& rm -rf "mysql-connector-java-${MYSQL_DRIVER_VERSION}" \  
&& chown ${RUN_USER}:${RUN_GROUP} ${CONFLUENCE_INSTALL_DIR}/confluence/WEB-
INF/lib/mysql-connector-java-${MYSQL_DRIVER_VERSION}.jar

