FROM openjdk:8u131-jdk  
  
# Install git, sendmail  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
git \  
sendmail \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ENV JENKINS_USER=jenkins \  
JENKINS_UID=1592 \  
JENKINS_GROUP=jenkins \  
JENKINS_GID=1592 \  
JENKINS_HOME=/var/jenkins \  
JENKINS_SLAVE_AGENT_PORT=50000 \  
JENKINS_EXECUTORS=2 \  
JENKINS_INSTALL_DIR=/usr/share/jenkins  
  
# User settings  
RUN addgroup \  
\--gid ${JENKINS_GID} \  
${JENKINS_GROUP} \  
&& adduser \  
\--uid ${JENKINS_UID} \  
\--ingroup ${JENKINS_GROUP} \  
\--home ${JENKINS_HOME} \  
\--shell /bin/bash \  
\--disabled-password \  
-c "Jenkins Account" \  
\--gecos "" \  
${JENKINS_USER}  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
ENV TINI_VERSION=0.14.0 \  
TINI_SHA=6c41ec7d33e857d4779f14d9c74924cab0c7973485d2972419a3b7c7620ff5fd  
  
RUN curl -fsSL
https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-
static-amd64 -o /bin/tini \  
&& chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha256sum -c -  
  
# Setting slave agent port  
COPY tcp-slave-agent-port.groovy executors.groovy
${JENKINS_INSTALL_DIR}/ref/init.groovy.d/  
  
# Install Jenkins  
ENV COPY_REFERENCE_FILE_LOG=${JENKINS_HOME}/copy_reference_file.log \  
JENKINS_VERSION=2.88  
COPY jenkins-support jenkins.sh docker-entrypoint.sh /usr/local/bin/  
  
RUN curl -fsSL https://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-
war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o
${JENKINS_INSTALL_DIR}/jenkins.war \  
&& chown -R ${JENKINS_USER}:${JENKINS_GROUP} ${JENKINS_INSTALL_DIR}/ref \  
&& chmod -R 755 /usr/local/bin  
  
USER root  
  
# Data mount  
VOLUME ${JENKINS_HOME}  
  
# HTTP & slave agent port  
EXPOSE 8080 ${JENKINS_SLAVE_AGENT_PORT}  
  
ENTRYPOINT [ "docker-entrypoint.sh" ]  
  
# Run in foreground  
CMD [ "sh", "-c", "su -s /bin/bash --preserve-environment -c '/bin/tini --
/usr/local/bin/jenkins.sh' ${JENKINS_USER}" ]  

