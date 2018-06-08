FROM openjdk:8-jre-alpine  
MAINTAINER Albert Tavares de Almeida <alberttava@gmail.com>  
  
ARG GO_PLUGIN_PATH=/opt/go-server/work/plugins/external  
  
# Set environment  
ENV GOCD_VERSION=16.12.0 \  
GOCD_RELEASE=go-server \  
GOCD_REVISION=4352 \  
GOCD_HOME=/opt/go-server \  
GOCD_PLUGIN_DIR=/opt/go-server/work/plugins/external \  
PATH=$GOCD_HOME:$PATH \  
USER_HOME=/root  
ENV
GOCD_REPO=https://download.go.cd/binaries/${GOCD_VERSION}-${GOCD_REVISION}/generic
\  
GOCD_RELEASE_ARCHIVE=${GOCD_RELEASE}-${GOCD_VERSION}-${GOCD_REVISION}.zip \  
SERVER_WORK_DIR=${GOCD_HOME}/work \  
GOCD_USER_FILE=${SERVER_WORK_DIR}/users.htpasswd  
  
# Install and configure gocd  
RUN apk add --no-cache --update git curl wget bash apache2-utils openssh ca-
certificates && rm -rf /var/cache/apk/* \  
&& mkdir /opt /var/log/go-server /var/run/go-server \  
&& cd /opt && curl -sSL ${GOCD_REPO}/${GOCD_RELEASE_ARCHIVE} -O && unzip
${GOCD_RELEASE_ARCHIVE} && rm ${GOCD_RELEASE_ARCHIVE} \  
&& mv /opt/${GOCD_RELEASE}-${GOCD_VERSION} ${GOCD_HOME} \  
&& chmod 774 ${GOCD_HOME}/*.sh  
  
#Add plugins  
RUN mkdir -p ${GOCD_PLUGIN_DIR}  
RUN wget -O ${GOCD_PLUGIN_DIR}/go-generic-artifactory-poller.jar
https://github.com/varchev/go-generic-artifactory-
poller/releases/download/0.2.0/go-generic-artifactory-poller.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/go-npm-poller.jar
https://github.com/varchev/go-npm-poller/releases/download/0.3.1/go-npm-
poller.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/go-artifactory-plugin-1.0.0-62.distribution.jar
https://github.com/tusharm/go-artifactory-
plugin/releases/download/v1.0.0-62/go-artifactory-
plugin-1.0.0-62.distribution.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/docker-task-assembly-0.1.27.jar
https://github.com/manojlds/gocd-docker/releases/download/0.1.27/docker-task-
assembly-0.1.27.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/script-executor-0.3.0.jar
https://github.com/gocd-contrib/script-executor-
task/releases/download/0.3/script-executor-0.3.0.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/gocd-gradle-plugin-1.0.6.jar
https://github.com/jmnarloch/gocd-gradle-plugin/releases/download/1.0.6/gocd-
gradle-plugin-1.0.6.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/gocd-docker-pipeline-plugin-1.0.0.jar
https://github.com/Haufe-Lexware/gocd-
plugins/releases/download/v1.0.0-beta/gocd-docker-pipeline-plugin-1.0.0.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/gocd-sonar-qualitygates-plugin-1.0.0.jar
https://github.com/Haufe-Lexware/gocd-
plugins/releases/download/v1.0.0-beta/gocd-sonar-qualitygates-plugin-1.0.0.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/gocd-slack-task-1.3.jar
https://github.com/Vincit/gocd-slack-task/releases/download/v1.3/gocd-slack-
task-1.3.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/email-notifier-0.1.jar https://github.com/gocd-
contrib/email-notifier/releases/download/v0.1/email-notifier-0.1.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/gocd-slack-notifier-1.4.0-RC11.jar
https://github.com/ashwanthkumar/gocd-slack-build-
notifier/releases/download/v1.4.0-RC11/gocd-slack-notifier-1.4.0-RC11.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/gocd-websocket-notifier.jar
https://github.com/matt-richardson/gocd-websocket-
notifier/releases/download/0.4.2%2Bbuild.60/gocd-websocket-notifier.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/go-artifactory-scm-plugin-0.6.jar
https://github.com/cnenning/go-artifactory-scm-
plugin/releases/download/0.6/go-artifactory-scm-plugin-0.6.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/go-artifactory-pkg-plugin-0.6.jar
https://github.com/cnenning/go-artifactory-scm-
plugin/releases/download/0.6/go-artifactory-pkg-plugin-0.6.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/go-cd-git-path-material-plugin-1.2.1.jar
https://github.com/TWChennai/gocd-git-path-material-
plugin/releases/download/1.2.1/go-cd-git-path-material-plugin-1.2.1.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/gitlab-oauth-login-2.2.jar
https://github.com/gocd-contrib/gocd-oauth-
login/releases/download/v2.2/gitlab-oauth-login-2.2.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/docker-elastic-agents-0.6.1.jar
https://github.com/gocd-contrib/docker-elastic-
agents/releases/download/v0.6.1/docker-elastic-agents-0.6.1.jar  
RUN wget -O ${GOCD_PLUGIN_DIR}/git-fb-poller-1.3.0-RC2.jar
https://github.com/ashwanthkumar/gocd-build-github-pull-
requests/releases/download/v1.3.0-RC2/git-fb-poller-1.3.0-RC2.jar  
  
# Add start script  
ADD docker-entrypoint.sh /usr/bin/docker-entrypoint.sh  
RUN chmod +x /usr/bin/docker-entrypoint.sh  
  
WORKDIR ${GOCD_HOME}  
  
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]  

