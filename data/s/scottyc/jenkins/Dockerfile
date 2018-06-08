FROM java:openjdk-8-jdk-alpine  
  
USER root  
  
RUN apk add --no-cache jq git curl zip unzip bash bash-doc bash-completion
ttf-dejavu openssh  
  
ENV JENKINS_HOME /home/jenkins  
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
  
# Jenkins home directory is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME /home/jenkins  
  
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
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.0}  
ARG JENKINS_SHA  
  
ENV JENKINS_SHA ${JENKINS_SHA:-da06f963edb627f0ced2fce612f9985d1928f79b}  
  
# could use ADD but this one does not check Last-Modified header  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fsSL http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-
war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o
/usr/share/jenkins/jenkins.war \  
&& echo "$JENKINS_SHA /usr/share/jenkins/jenkins.war" | sha1sum -c -  
  
ENV JENKINS_UC https://updates.jenkins-ci.org  
RUN chown -R ${user} "$JENKINS_HOME" /usr/share/jenkins/ref  
  
# for main web interface, slave agents and SSH port  
EXPOSE 8080 50000 22  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
USER root  
  
COPY basic-security.groovy /home/jenkins/init.groovy.d/  
COPY jenkins.install.UpgradeWizard.state /home/jenkins/  
  
RUN mkdir -p /home/jenkins/jobs/  
RUN mkdir -p /home/jenkins/users/  
COPY credentials/credentials.xml /home/jenkins/credentials.xml  
  
# #Set up Job-DSL  
COPY jobs/seed.xml /home/jenkins/seed.xml  
COPY jobs/seed.groovy home/jenkins/  
COPY jobs/build.sh /home/jenkins/  
  
# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY plugins.txt /usr/share/jenkins/ref/  
RUN chown jenkins:jenkins /usr/local/bin/plugins.sh  
RUN chown jenkins:jenkins -R /home/jenkins/  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt  
  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  

