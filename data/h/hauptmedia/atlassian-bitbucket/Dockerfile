FROM atlassian/bitbucket-server:5.8.0  
MAINTAINER Julian Haupt <julian.haupt@hauptmedia.de>  
  
ENV MYSQL_CONNECTOR_J_VERSION 5.1.45  
# integrate mysql connector j library  
RUN curl -L http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_CONNECTOR_J_VERSION}.tar.gz | tar -xz -C /tmp && \  
cp /tmp/mysql-connector-java-${MYSQL_CONNECTOR_J_VERSION}/mysql-connector-
java-${MYSQL_CONNECTOR_J_VERSION}-bin.jar /opt/atlassian/bitbucket/lib && \  
rm -rf /tmp/*  

