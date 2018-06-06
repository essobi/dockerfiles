# Docker image for CloudBees Jenkins Operations Center  
FROM java:8-jdk  
MAINTAINER Harshal Dharia <hdharia@cloudbees.com>  
RUN apt-get update && apt-get install -y wget git curl zip && rm -rf
/var/lib/apt/lists/*  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV SSHD_HOST jenkins.beedemo.local  
ENV JENKINS_PREFIX /cjoc  
ENV JENKINS_JNLP_PORT 4001  
ENV JENKINS_SSH_PORT 2021  
ENV JENKINS_HTTP_PORT 8080  
ENV JENKINS_URL http://jenkins.beedemo.local:8080/cjoc  
#when setting up in HA, set to flase to skip copying ref files and plugins as
that only needs to be done once per HA cluster  
ENV COPY_REF_FILES true  
  
# Jenkins is ran with user `jenkins`, uid = 1000  
# If you bind mount a volume from host/volume from a data container,  
# ensure you use same uid  
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins  
  
# Jenkins home directoy is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME $JENKINS_HOME  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
ENV TINI_SHA 066ad710107dc7ee05d3aa6e4974f01dc98f3888  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fL https://github.com/krallin/tini/releases/download/v0.5.0/tini-
static -o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha1sum -c -  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/init_00_fixed-
ports_url.groovy  
COPY init-disable.groovy
/usr/share/jenkins/ref/init.groovy.d/init_99_disable.groovy  
  
ENV JENKINS_VERSION 1.625.18.5  
# https://repo-internal.cloudbees.com/com/cloudbees/operations-
center/server/operations-center-war/$JENKINS_VERSION/operations-center-
war-$JENKINS_VERSION.war.sha1  
ENV JENKINS_SHA fbc8b73bc655d43f15f3ede4e94fbe4a50b64ae3  
  
# could use ADD but this one does not check Last-Modified header  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fL http://jenkins-
updates.cloudbees.com/download/oc/$JENKINS_VERSION/jenkins-oc.war -o
/usr/share/jenkins/jenkins.war \  
&& echo "$JENKINS_SHA /usr/share/jenkins/jenkins.war" | sha1sum -c -  
  
ENV JENKINS_UC https://updates.jenkins-ci.org  
RUN chown -R jenkins "$JENKINS_HOME" /usr/share/jenkins/ref  
  
# for main web interface:  
EXPOSE 8080  
# jnlp port used to connect client masters:  
EXPOSE 4001  
# will be used for ssh:  
EXPOSE 2021  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
USER jenkins  
  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  

