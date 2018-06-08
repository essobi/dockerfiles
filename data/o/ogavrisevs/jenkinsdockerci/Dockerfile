FROM java:8-jdk  
  
RUN apt-get update && apt-get install -y wget git curl zip tree awscli && rm
-rf /var/lib/apt/lists/*  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
# Jenkins is run with user `jenkins`, uid = 1000  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins  
  
# Jenkins home directory is a volume, so configuration and build history  
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
  
COPY groovy/*.groovy /usr/share/jenkins/ref/init.groovy.d/  
COPY job-dsl/*.json /usr/share/jenkins/ref/init.groovy.d/job-dsl/  
COPY cloud-init/*.yaml /usr/share/jenkins/ref/init.groovy.d/cloud-init/  
  
ENV JENKINS_VERSION 1.625.3  
ENV JENKINS_SHA 537d910f541c25a23499b222ccd37ca25e074a0c  
  
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
  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY plugins.txt /usr/local/bin/plugins.txt  
RUN chown jenkins:jenkins /usr/local/bin/jenkins.sh /usr/local/bin/plugins.sh
/usr/local/bin/plugins.txt  
  
USER jenkins  
  
RUN /usr/local/bin/plugins.sh /usr/local/bin/plugins.txt  
  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  

