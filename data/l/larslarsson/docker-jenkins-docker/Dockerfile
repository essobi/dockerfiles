FROM java:8-jdk  
  
RUN apt-get update && apt-get install -y wget git curl zip sudo && rm -rf
/var/lib/apt/lists  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins  
  
VOLUME /var/jenkins_home  
  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
ENV TINI_SHA 066ad710107dc7ee05d3aa6e4974f01dc98f3888  
  
RUN curl -fL https://github.com/krallin/tini/releases/download/v0.5.0/tini-
static -o /bin/tini && chmod +x /bin/tini  
RUN echo "$TINI_SHA /bin/tini" | sha1sum -c -  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
  
ENV JENKINS_VERSION 1.642.2  
ENV JENKINS_SHA e72e06e64d23eefb13090459f517b0697aad7be0  
  
  
RUN curl -fL http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-
war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o
/usr/share/jenkins/jenkins.war  
RUN echo "$JENKINS_SHA /usr/share/jenkins/jenkins.war" | sha1sum -c -  
  
ENV JENKINS_UC https://updates.jenkins-ci.org  
RUN chown -R jenkins "$JENKINS_HOME" /usr/share/jenkins/ref  
RUN chown -R jenkins /var/jenkins_home  
EXPOSE 8080  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
COPY plugins.sh /usr/local/bin/plugins.sh  
  
# Install docker  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
RUN curl -fsSL https://get.docker.com/gpg | apt-key add -  
RUN curl -fsSL https://get.docker.com/ | sh  
RUN usermod -aG docker jenkins  
  
# Install docker-compose  
RUN curl -L https://github.com/docker/compose/releases/download/1.6.2/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
  
RUN chmod +x /usr/local/bin/jenkins.sh  
RUN chown -R 1000 /var/jenkins_home  
USER jenkins  
  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  

