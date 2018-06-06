FROM java:7  
  
# Setup useful environment variables  
ENV CONF_HOME /var/atlassian/confluence  
ENV CONF_INSTALL /opt/atlassian/confluence  
ENV CONF_VERSION 5.1.4  
  
# Install Atlassian Confluence  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get clean \  
&& mkdir -p "${CONF_HOME}" \  
&& chmod -R 700 "${CONF_HOME}" \  
&& chown daemon:daemon "${CONF_HOME}" \  
&& mkdir -p "${CONF_INSTALL}" \  
&& curl -Ls
"https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONF_VERSION}.tar.gz" | tar -xz --directory "${CONF_INSTALL}"
\--strip-components=1 --no-same-owner \  
&& curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.39.tar.gz" | tar -xz --directory "${CONF_INSTALL}/confluence/WEB-
INF/lib" \--strip-components=1 --no-same-owner "mysql-connector-
java-5.1.39/mysql-connector-java-5.1.39-bin.jar" \  
&& echo -e "\nconfluence.home=$CONF_HOME" >> "${CONF_INSTALL}/confluence/WEB-
INF/classes/confluence-init.properties" \  
&& chmod -R 777 "${CONF_INSTALL}" \  
&& chown -R daemon:daemon "${CONF_INSTALL}"  
  
USER daemon:daemon  
  
EXPOSE 8090  
  
VOLUME ["/var/atlassian/confluence", "/opt/atlassian/confluence/logs"]  
  
WORKDIR /var/atlassian/confluence  
  
CMD ["/opt/atlassian/confluence/bin/catalina.sh", "run"]  

