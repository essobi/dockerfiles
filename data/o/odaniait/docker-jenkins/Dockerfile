FROM odaniait/docker-base-java:latest  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
## Install jenkins runit service  
RUN mkdir /etc/service/jenkins  
COPY runit/jenkins.sh /etc/service/jenkins/run  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
# Jenkins is run with user `jenkins`, uid = 1000  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
COPY groovy/init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
COPY groovy/executors.groovy
/usr/share/jenkins/ref/init.groovy.d/executors.groovy  
  
ENV JENKINS_VERSION 1.625.3  
ENV JENKINS_SHA 537d910f541c25a23499b222ccd37ca25e074a0c  
  
# could use ADD but this one does not check Last-Modified header  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fL http://mirrors.jenkins-ci.org/war-
stable/$JENKINS_VERSION/jenkins.war -o /usr/share/jenkins/jenkins.war \  
&& echo "$JENKINS_SHA /usr/share/jenkins/jenkins.war" | sha1sum -c -  
  
ENV JENKINS_UC https://updates.jenkins-ci.org  
RUN chown -R jenkins:jenkins "$JENKINS_HOME" /usr/share/jenkins/ref  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY runit/jenkins.sh /usr/local/bin/jenkins.sh  
  
# Jenkins home directory is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME ['/var/jenkins_home']  
  
# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
  
WORKDIR /var/jenkins_home  

