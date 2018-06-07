FROM insanitydesign/jira-software-server  
MAINTAINER INsanityDesign  
  
# MySQL Connector/J Version  
ENV MYSQL_DRIVER_VERSION 5.1.46  
# Download and copy the MySQL connector into the Jira instance  
RUN cd /tmp && wget "https://dev.mysql.com/get/Downloads/Connector-J/mysql-
connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& tar -xzf "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& mv "mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.jar" "${JIRA_INSTALL_DIR}/lib/." \  
&& rm "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& rm -rf "mysql-connector-java-${MYSQL_DRIVER_VERSION}" \  
&& chown ${RUN_USER}:${RUN_GROUP} ${JIRA_INSTALL_DIR}/lib/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.jar  

