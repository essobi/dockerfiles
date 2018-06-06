# This builds a Confluence Docker container  
FROM inftec/ubuntu-java:8u121-certs  
MAINTAINER Fabian Gut <fabian.gut@inftec.ch>, InfTec GmbH  
MAINTAINER Martin Meyer <martin.meyer@inftec.ch>, InfTec GmbH  
  
# Install Curl  
RUN apt-get update && \  
apt-get install -y \  
curl && \  
apt-get autoclean  
  
# Download MYSQL Driver - this is done first, as the version changes less
frequently as the confluence version  
ENV MYSQL_DRIVER_VERSION 5.1.40  
RUN curl -Lks http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz -o /root/mysql-connector.tar.gz  
  
# Install Confluence  
ENV CONF_VERSION 6.8.1  
RUN curl -Lks
http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONF_VERSION}.tar.gz -o /root/confluence.tar.gz  
RUN mkdir /opt/confluence && tar xzf /root/confluence.tar.gz --strip=1 -C
/opt/confluence && rm /root/confluence.tar.gz  
  
# Install MYSQL Driver  
RUN tar xzf /root/mysql-connector.tar.gz --strip=1 --wildcards '*/mysql-
connector-java*.jar' && \  
mv mysql-connector-java*.jar /opt/confluence/confluence/WEB-INF/lib && \  
rm /root/mysql-connector.tar.gz  
  
# Copy assets  
COPY assets/setup/ /opt/conf-setup/setup/  
COPY assets/conf.init /opt/conf-setup/conf.init  
RUN mkdir -p /opt/conf-setup/config && cp /opt/confluence/conf/server.xml
/opt/conf-setup/config/server.xml  
RUN chmod 755 /opt/conf-setup/conf.init  
  
VOLUME /opt/confluence-home  
EXPOSE 8090 8091  
ENTRYPOINT ["/opt/conf-setup/conf.init"]  
CMD ["conf:start"]  
  

