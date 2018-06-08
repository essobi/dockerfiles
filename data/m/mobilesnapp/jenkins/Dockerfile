############################################  
# Dockerfile to build Jenkins service image  
############################################  
# Base image  
FROM ubuntu:14.04  
# Author: MobileSnapp Inc.  
MAINTAINER MobileSnapp <support@mobilesnapp.com>  
  
# Install essentials.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update -q && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
apt-get --no-install-recommends install -q -y openjdk-7-jre-headless && \  
apt-get install git curl wget zip mysql-client -y -q && \  
rm -rf /var/lib/apt/lists/*  
  
# Set environment variables.  
ENV HOME /root  
ENV JENKINS_PREFIX /  
ENV JENKINS_HOME /var/jenkins_home  
ENV JAVA_ARGS -Xmx2048m -XX:MaxPermSize=512m  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
# Set user data.  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
# Jenkins is run with user `jenkins`, uid = 1000  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
RUN groupadd -g ${gid} ${group} \  
&& useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}  
  
# Jenkins home directory is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME /var/jenkins_home  
  
RUN mkdir -p /opt/jenkins  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
ENV TINI_SHA 066ad710107dc7ee05d3aa6e4974f01dc98f3888  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fsSL https://github.com/krallin/tini/releases/download/v0.5.0/tini-
static -o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha1sum -c -  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
  
ARG JENKINS_VERSION  
ENV JENKINS_VERSION ${JENKINS_VERSION:-1.651.2}  
ARG JENKINS_SHA  
ENV JENKINS_SHA ${JENKINS_SHA:-f61b8b604acba5076a93dcde28c0be2561d17bde}  
  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fsSL http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-
war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o
/usr/share/jenkins/jenkins.war \  
&& echo "$JENKINS_SHA /usr/share/jenkins/jenkins.war" | sha1sum -c -  
  
ENV JENKINS_UC https://updates.jenkins.io  
RUN chown -R ${user} "$JENKINS_HOME" /usr/share/jenkins/ref  
  
# Expose ports  
# For main web interface:  
EXPOSE 8080  
# For attached slave agents:  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
USER ${user}  
  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  
# From a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY install-plugins.sh /usr/local/bin/install-plugins.sh

