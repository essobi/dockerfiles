FROM openjdk:8-jdk-alpine  
MAINTAINER Dave Chevell  
  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
#
https://confluence.atlassian.com/display/JSERVERM/Important+directories+and+files  
ENV JIRA_HOME /var/atlassian/application-data/jira  
ENV JIRA_INSTALL_DIR /opt/atlassian/jira  
  
VOLUME ["${JIRA_HOME}"]  
  
# Expose HTTP port  
EXPOSE 8080  
WORKDIR $JIRA_HOME  
  
CMD ["/entrypoint.sh", "-fg"]  
ENTRYPOINT ["/sbin/tini", "--"]  
  
RUN apk update -qq \  
&& update-ca-certificates \  
&& apk add ca-certificates wget curl openssh bash procps openssl perl ttf-
dejavu tini \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
COPY entrypoint.sh /entrypoint.sh  
  
ARG JIRA_VERSION=7.2.15  
ARG
DOWNLOAD_URL=https://www.atlassian.com/software/jira/downloads/binary/atlassian-
jira-software-${JIRA_VERSION}.tar.gz  
  
COPY . /tmp  
  
RUN mkdir -p ${JIRA_INSTALL_DIR} \  
&& curl -L --silent ${DOWNLOAD_URL} | tar -xz --strip-components=1 -C
"$JIRA_INSTALL_DIR" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${JIRA_INSTALL_DIR}/ \  
&& sed -i -e 's/^JVM_SUPPORT_RECOMMENDED_ARGS=""$/:
\${JVM_SUPPORT_RECOMMENDED_ARGS:=""}/g' ${JIRA_INSTALL_DIR}/bin/setenv.sh \  
&& sed -i -e 's/^JVM_\\(.*\\)_MEMORY="\\(.*\\)"$/: \${JVM_\1_MEMORY:=\2}/g'
${JIRA_INSTALL_DIR}/bin/setenv.sh \  
&& sed -i -e 's/grep "java version"/grep -E "(openjdk|java) version"/g'
${JIRA_INSTALL_DIR}/bin/check-java.sh \  
&& sed -i -e 's/port="8080"/port="8080" secure="${catalinaConnectorSecure}"
scheme="${catalinaConnectorScheme}" proxyName="${catalinaConnectorProxyName}"
proxyPort="${catalinaConnectorProxyPort}"/'
${JIRA_INSTALL_DIR}/conf/server.xml  

