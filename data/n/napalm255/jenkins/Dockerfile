FROM fedora:23  
USER root  
  
RUN dnf -y update  
  
# python 2  
RUN dnf -y install python  
RUN /usr/bin/python2 -m pip install pip --upgrade  
RUN /usr/bin/python2 -m pip install virtualenv --upgrade  
  
# python 3  
RUN dnf -y install python3  
RUN /usr/bin/python3 -m pip install pip --upgrade  
RUN /usr/bin/python3 -m pip install virtualenv --upgrade  
  
# tools  
RUN dnf -y install git curl zip wget  
  
# java  
RUN dnf -y install java  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
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
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
  
USER ${user}  
  
# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  

