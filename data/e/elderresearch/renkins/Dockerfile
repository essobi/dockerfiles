# This is a fork of the official Jenkins Docker image, but modified to be  
# based on an enhanced R Docker images so that Jenkins jobs using R can be
run.  
FROM rocker/hadleyverse  
  
MAINTAINER "Simeon H.K. Fitch" fitch@datamininglab.com  
  
USER root  
  
ENV JENKINS_UID 2000  
# network discovery UDP port  
ENV JENKINS_UDP_PORT 33848  
EXPOSE 33848  
# Everything between the lines is from the official Jenkins image.  
#-----------------------------------------------------------------  
RUN apt-get update && apt-get install -y wget git curl zip && rm -rf
/var/lib/apt/lists/*  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
# Jenkins is ran with user `jenkins`, uid = 1000  
# If you bind mount a volume from host/volume from a data container,  
# ensure you use same uid  
RUN useradd -d "$JENKINS_HOME" -u $JENKINS_UID -m -s /bin/bash jenkins  
  
# Jenkins home directoy is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME /var/jenkins_home  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
ENV TINI_SHA 066ad710107dc7ee05d3aa6e4974f01dc98f3888  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fL https://github.com/krallin/tini/releases/download/v0.5.0/tini-
static -o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha1sum -c -  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
  
ENV JENKINS_VERSION 1.625.1  
ENV JENKINS_SHA c96d44d4914a154c562f21cd20abdd675ac7f5f3  
  
# could use ADD but this one does not check Last-Modified header  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fL http://mirrors.jenkins-ci.org/war-
stable/$JENKINS_VERSION/jenkins.war -o /usr/share/jenkins/jenkins.war \  
&& echo "$JENKINS_SHA /usr/share/jenkins/jenkins.war" | sha1sum -c -  
  
ENV JENKINS_UC https://updates.jenkins-ci.org  
RUN chown -R jenkins "$JENKINS_HOME" /usr/share/jenkins/ref  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
USER jenkins  
  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  
# from a derived Dockerfile, can use `RUN plugin.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
  
#-----------------------------------------------------------------  
# Everything between the lines is from the official Jenkins image.  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
  

