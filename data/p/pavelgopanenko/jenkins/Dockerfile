FROM java:openjdk-7u65-jdk  
  
MAINTAINER Pavel Gopanenko <pgopanenko@gmail.com>  
  
RUN apt-get update && apt-get install -y wget git mercurial curl zip unzip &&
rm -rf /var/lib/apt/lists/*  
  
ENV JENKINS_HOME /var/jenkins_home  
  
# Jenkins is ran with user `jenkins`, uid = 1000  
# If you bind mount a volume from host/vloume from a data container,  
# ensure you use same uid  
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins  
  
# Jenkins home directoy is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME /var/jenkins_home  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-angent-
port.groovy  
  
ENV JENKINS_VERSION 1.638  
# could use ADD but this one does not check Last-Modified header  
# see https://github.com/docker/docker/issues/8331  
RUN curl -L http://mirrors.jenkins-ci.org/war/$JENKINS_VERSION/jenkins.war -o
/usr/share/jenkins/jenkins.war  
  
ENV JENKINS_UC https://updates.jenkins-ci.org  
ENV JENKINS_REF /usr/share/jenkins/ref  
  
RUN mkdir -p $JENKINS_REF/plugins  
RUN mkdir -p $JENKINS_REF/jobs  
RUN chown -R jenkins $JENKINS_REF  
  
USER jenkins  
  
RUN curl -L $JENKINS_UC/latest/greenballs.hpi -o
$JENKINS_REF/plugins/greenballs.hpi && \  
curl -L $JENKINS_UC/latest/versionnumber.hpi -o
$JENKINS_REF/plugins/versionnumber.hpi && \  
curl -L $JENKINS_UC/latest/swarm.hpi -o $JENKINS_REF/plugins/swarm.hpi && \  
curl -L $JENKINS_UC/latest/credentials.hpi -o
$JENKINS_REF/plugins/credentials.hpi && \  
curl -L $JENKINS_UC/latest/ssh-credentials.hpi -o $JENKINS_REF/plugins/ssh-
credentials.hpi && \  
curl -L $JENKINS_UC/latest/matrix-project.hpi -o $JENKINS_REF/plugins/matrix-
project.hpi && \  
curl -L $JENKINS_UC/latest/multiple-scms.hpi -o $JENKINS_REF/plugins/multiple-
scms.hpi && \  
curl -L $JENKINS_UC/latest/scm-api.hpi -o $JENKINS_REF/plugins/scm-api.hpi &&
\  
curl -L $JENKINS_UC/latest/mercurial.hpi -o $JENKINS_REF/plugins/mercurial.hpi
&& \  
curl -L $JENKINS_UC/latest/promoted-builds.hpi -o
$JENKINS_REF/plugins/promoted-builds.hpi && \  
curl -L $JENKINS_UC/latest/maven-plugin.hpi -o $JENKINS_REF/plugins/maven-
plugin.hpi && \  
curl -L $JENKINS_UC/latest/token-macro.hpi -o $JENKINS_REF/plugins/token-
macro.hpi && \  
curl -L $JENKINS_UC/latest/mailer.hpi -o $JENKINS_REF/plugins/mailer.hpi && \  
curl -L $JENKINS_UC/latest/javadoc.hpi -o $JENKINS_REF/plugins/javadoc.hpi &&
\  
curl -L $JENKINS_UC/latest/parameterized-trigger.hpi -o
$JENKINS_REF/plugins/parameterized-trigger.hpi && \  
curl -L $JENKINS_UC/latest/conditional-buildstep.hpi -o
$JENKINS_REF/plugins/conditional-buildstep.hpi && \  
curl -L $JENKINS_UC/latest/run-condition.hpi -o $JENKINS_REF/plugins/run-
condition.hpi && \  
curl -L $JENKINS_UC/latest/git-client.hpi -o $JENKINS_REF/plugins/git-
client.hpi && \  
curl -L $JENKINS_UC/latest/git.hpi -o $JENKINS_REF/plugins/git.hpi  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
ENTRYPOINT ["/usr/local/bin/jenkins.sh"]  

