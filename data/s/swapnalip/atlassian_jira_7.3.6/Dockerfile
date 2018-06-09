FROM openjdk:8  
MAINTAINER Swapnali Pingale <yeole.swapnali@gmail.com>  
  
ENV JIRA_VERSION 7.3.6  
ENV JIRA_HOME "/var/atlassian/jira"  
ENV JIRA_INSTALL "/opt/atlassian/jira"  
ENV DOWNLOAD_URL
"https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-
core-"  
ENV JVM_MYSQL_CONNECTOR_URL "http://dev.mysql.com/get/Downloads/Connector-J"  
ENV JVM_MYSQL_CONNETOR "mysql-connector-java-5.1.38"  
RUN apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends -t jessie-backports
libtcnative-1 \  
&& apt-get clean  
  
RUN mkdir -p ${JIRA_HOME} \  
${JIRA_HOME}/lib \  
${JIRA_HOME}/caches/indexes \  
${JIRA_INSTALL}/conf/Catalina \  
${JIRA_INSTALL}/lib \  
&& curl -Ls "${DOWNLOAD_URL}${JIRA_VERSION}.tar.gz" | tar -xz --directory
"${JIRA_INSTALL}" \--strip=1 \  
&& curl -Ls "${JVM_MYSQL_CONNECTOR_URL}/${JVM_MYSQL_CONNETOR}.tar.gz" | tar
-xz --directory "${JIRA_INSTALL}/lib" \--strip=1 --no-same-owner
"${JVM_MYSQL_CONNETOR}/${JVM_MYSQL_CONNETOR}-bin.jar" \  
&& sed --in-place "s/java version/openjdk version/g"
"${JIRA_INSTALL}/bin/check-java.sh" \  
&& echo -e "\njira.home=$JIRA_HOME" >> "${JIRA_INSTALL}/atlassian-jira/WEB-
INF/classes/jira-application.properties" \  
&& chmod -R 700 ${JIRA_HOME} ${JIRA_INSTALL}  
  
EXPOSE 8080  
VOLUME ["/var/atlassian/jira", "/opt/atlassian/jira/logs"]  
  
WORKDIR /opt/atlassian/jira  
  
COPY "docker-entrypoint.sh" "/"  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/opt/atlassian/jira/bin/catalina.sh", "run"]  

