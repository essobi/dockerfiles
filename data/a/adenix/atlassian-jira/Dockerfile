FROM adenix/oracle-java:8-jre  
  
ARG JIRA_VERSION=7.7.1  
ARG
DOWNLOAD_URL=https://www.atlassian.com/software/jira/downloads/binary/atlassian-
jira-software-${JIRA_VERSION}.tar.gz  
  
ENV \  
RUN_USER=daemon \  
RUN_GROUP=daemon \  
JIRA_HOME=/var/atlassian/application-data/jira \  
JIRA_INSTALL=/opt/atlassian/jira  
  
WORKDIR $JIRA_INSTALL  
  
# Expose HTTP, HTTPS  
EXPOSE 8080  
EXPOSE 8443  
VOLUME ["${JIRA_HOME}"]  
  
CMD ["/docker-entrypoint.sh", "-fg"]  
  
RUN \  
mkdir -p ${JIRA_INSTALL} && \  
curl -L --silent ${DOWNLOAD_URL} | tar -xz --strip-components=1 -C
$JIRA_INSTALL && \  
chown -R ${RUN_USER}:${RUN_GROUP} ${JIRA_INSTALL}/ && \  
sed -i -e 's/-Xms\\([0-9]\\+[kmg]\\)
-Xmx\\([0-9]\\+[kmg]\\)/-Xms\${JVM_MINIMUM_MEMORY:=\1}
-Xmx\${JVM_MAXIMUM_MEMORY:=\2} \${JVM_SUPPORT_RECOMMENDED_ARGS}
-Djira.home=\${JIRA_HOME}/g' ${JIRA_INSTALL}/bin/setenv.sh  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
COPY server.xml ${JIRA_INSTALL}/conf/server.xml  

