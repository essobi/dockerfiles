FROM debian:stretch-slim  
  
MAINTAINER wilkesystems <maintainer@wilke.systems>  
  
ENV CONFLUENCE_VERSION=6.7.2  
ENV CONFLUENCE_HOME=/var/atlassian/application-data/confluence  
ENV CONFLUENCE_INSTALL_DIR=/opt/atlassian/confluence  
  
ARG
CONFLUENCE_BINARY=https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONFLUENCE_VERSION}-x64.bin  
ARG
MYSQL_CONNECTOR_JAVA=https://dev.mysql.com/get/Downloads/Connector-J/mysql-
connector-java-5.1.45.tar.gz  
  
RUN apt-get update; \  
apt-get install -y ca-certificates curl git locales locales-all openssl perl
procps ttf-dejavu wget; \  
bash -c 'mkdir -m 755 -p /usr/share/atlassian/confluence/{driver,install}'; \  
curl -sSL ${CONFLUENCE_BINARY} -o
/usr/share/atlassian/confluence/install/atlassian-
confluence-${CONFLUENCE_VERSION}-x64.bin; \  
chmod +x /usr/share/atlassian/confluence/install/atlassian-
confluence-${CONFLUENCE_VERSION}-x64.bin; \  
curl -sSL ${MYSQL_CONNECTOR_JAVA} | tar xz --directory
"/usr/share/atlassian/confluence/driver/" \--strip-components=1 --no-same-
owner \  
"mysql-connector-java-5.1.45/mysql-connector-java-5.1.45-bin.jar"; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*;  
  
COPY docker-entrypoint.sh /usr/sbin/docker-entrypoint.sh  
  
EXPOSE 8090 8091  
WORKDIR ${CONFLUENCE_HOME}  
  
CMD ["${CONFLUENCE_INSTALL_DIR}/bin/start-confluence.sh", "-fg"]  
  
ENTRYPOINT ["docker-entrypoint.sh"]  

