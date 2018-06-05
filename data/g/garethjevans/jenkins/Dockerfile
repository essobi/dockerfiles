FROM openjdk:8u151-jdk-alpine  
  
RUN apk add --no-cache git openssh-client wget curl unzip bash ttf-dejavu
coreutils  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
# Jenkins is run with user `jenkins`, uid = 1000  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
RUN addgroup -g ${gid} ${group} \  
&& adduser -h "$JENKINS_HOME" -u ${uid} -G ${group} -s /bin/bash -D ${user}  
  
RUN id jenkins  
  
# Jenkins home directoy is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
# VOLUME /var/jenkins_home  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
ENV TINI_VERSION 0.14.0  
ENV TINI_SHA 6c41ec7d33e857d4779f14d9c74924cab0c7973485d2972419a3b7c7620ff5fd  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fsSL
https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-
static-amd64 -o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha256sum -c -  
  
# COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
# jenkins version being bundled in this docker image  
ARG JENKINS_VERSION  
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.89.4}  
  
# Can be used to customize where jenkins.war get downloaded from  
ARG JENKINS_URL=https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war  
  
# could use ADD but this one does not check Last-Modified header neither does
it allow to control checksum  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fsSL ${JENKINS_URL} -o /usr/share/jenkins/jenkins.war  
  
ENV JENKINS_UC https://updates.jenkins-ci.org  
RUN chown -R jenkins "$JENKINS_HOME" /usr/share/jenkins/ref  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
COPY jenkins-support /usr/local/bin/jenkins-support  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY install-plugins.sh /usr/local/bin/install-plugins.sh  
  
RUN chown jenkins:jenkins /usr/local/bin/* && \  
chmod a+x /usr/local/bin/*  
  
RUN mkdir /opt  
  
ENV NEWRELIC_AGENT_VERSION 3.36.0  
RUN wget --quiet https://download.run.pivotal.io/new-relic/new-
relic-${NEWRELIC_AGENT_VERSION}.jar && \  
mkdir /opt/newrelic && \  
mv new-relic-${NEWRELIC_AGENT_VERSION}.jar /opt/newrelic/new-relic.jar && \  
chown -R jenkins:jenkins /opt/newrelic  
  
COPY newrelic.yml /opt/newrelic/  
  
USER jenkins  
  
# Install plugins  
COPY plugins.txt /usr/local/etc/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/local/etc/plugins.txt  
  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  

