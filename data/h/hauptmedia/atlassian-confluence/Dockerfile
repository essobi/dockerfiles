FROM hauptmedia/java:oracle-java8  
MAINTAINER Julian Haupt <julian.haupt@hauptmedia.de>  
  
ENV CONFLUENCE_VERSION 6.0.7  
ENV MYSQL_CONNECTOR_J_VERSION 5.1.34  
ENV CONFLUENCE_HOME /var/atlassian/application-data/confluence  
ENV CONFLUENCE_INSTALL_DIR /opt/atlassian/confluence  
  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install needed debian packages & clean up  
RUN apt-get update && \  
apt-get install -y --no-install-recommends curl tar xmlstarlet ca-certificates
&& \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
# download and extract confluence  
RUN mkdir -p ${CONFLUENCE_INSTALL_DIR} && \  
curl -L --silent
http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONFLUENCE_VERSION}.tar.gz | tar -xz --strip=1 -C
${CONFLUENCE_INSTALL_DIR} && \  
echo -e "\nconfluence.home=$CONFLUENCE_HOME" >>
"${CONFLUENCE_INSTALL_DIR}/confluence/WEB-INF/classes/confluence-
init.properties" && \  
chown -R ${RUN_USER}:${RUN_GROUP} ${CONFLUENCE_INSTALL_DIR}  
  
# integrate mysql connector j library  
RUN curl -L --silent http://dev.mysql.com/get/Downloads/Connector-J/mysql-
connector-java-${MYSQL_CONNECTOR_J_VERSION}.tar.gz | tar -xz --strip=1 -C /tmp
&& \  
cp /tmp/mysql-connector-java-${MYSQL_CONNECTOR_J_VERSION}-bin.jar
${CONFLUENCE_INSTALL_DIR}/confluence/WEB-INF/lib && \  
rm -rf /tmp/*  
  
# add docker-entrypoint.sh script  
COPY docker-entrypoint.sh ${CONFLUENCE_INSTALL_DIR}/bin/  
  
USER ${RUN_USER}:${RUN_GROUP}  
  
EXPOSE 8090  
WORKDIR ${CONFLUENCE_INSTALL_DIR}  
ENTRYPOINT ["bin/docker-entrypoint.sh"]  
CMD ["bin/start-confluence.sh", "-fg"]  

