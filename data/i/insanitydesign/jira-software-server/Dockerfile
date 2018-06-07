FROM openjdk:8-jdk-alpine  
MAINTAINER INsanityDesign  
  
# User and group for the running Jira instance  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
# Main directories  
ENV JIRA_HOME /var/atlassian/application-data/jira  
ENV JIRA_INSTALL_DIR /opt/atlassian/jira  
  
VOLUME ["${JIRA_HOME}"]  
  
# Expose Server and Connector ports  
EXPOSE 8005  
EXPOSE 8080  
# Home as main working directory  
WORKDIR $JIRA_HOME  
  
# Entrypoint to start Jira  
CMD ["/entrypoint.sh", "-fg"]  
ENTRYPOINT ["/sbin/tini", "--"]  
  
# Install some required packages  
RUN apk update -qq && update-ca-certificates && apk add ca-certificates wget
curl openssh bash procps openssl perl ttf-dejavu tini libc6-compat && rm -rf
/var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
# Copy the start script  
COPY entrypoint.sh /entrypoint.sh  
RUN ["chmod", "a+x", "/entrypoint.sh"]  
  
# Set the required download/version arguments  
ARG JIRA_VERSION=7.10.0  
ARG
DOWNLOAD_URL=https://www.atlassian.com/software/jira/downloads/binary/atlassian-
jira-software-${JIRA_VERSION}.tar.gz  
  
COPY . /tmp  
  
# Download and setup Jira  
RUN mkdir -p ${JIRA_INSTALL_DIR} \  
&& curl -L --silent ${DOWNLOAD_URL} | tar -xz --strip-components=1 -C
"$JIRA_INSTALL_DIR" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${JIRA_INSTALL_DIR}/ \  
&& sed -i -e 's/java version/openjdk version/g' ${JIRA_INSTALL_DIR}/bin/check-
java.sh \  
&& sed -i -e 's/-Xms\\([0-9]\\+[kmg]\\)
-Xmx\\([0-9]\\+[kmg]\\)/-Xms\${JVM_MINIMUM_MEMORY:=\1}
-Xmx\${JVM_MAXIMUM_MEMORY:=\2} \${JVM_SUPPORT_RECOMMENDED_ARGS}
-Djira.home=\${JIRA_HOME}/g' ${JIRA_INSTALL_DIR}/bin/setenv.sh \  
&& sed -i -e 's/port="8080"/port="8080" secure="${catalinaConnectorSecure}"
scheme="${catalinaConnectorScheme}" proxyName="${catalinaConnectorProxyName}"
proxyPort="${catalinaConnectorProxyPort}"/'
${JIRA_INSTALL_DIR}/conf/server.xml  

