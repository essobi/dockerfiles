#  
#  
#  
FROM appsoa/docker-centos-base-java:latest  
  
USER root  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
ENV JENKINS_UC https://updates.jenkins.io  
ENV COPY_REFERENCE_FILE_LOG /var/jenkins_home/copy_reference_file.log  
  
RUN useradd -d /var/jenkins_home -m -s /bin/bash jenkins  
  
# Jenkins home directory is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME /var/jenkins_home  
  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d && \  
curl -fsSL https://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-
war/2.4/jenkins-war-2.4.war -o /usr/share/jenkins/jenkins.war && \  
chown -R jenkins /var/jenkins_home /usr/share/jenkins  
  
COPY src/init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
COPY src/jenkins-support /usr/local/bin/jenkins-support  
COPY src/jenkins.sh /usr/local/bin/jenkins.sh  
COPY src/plugins.sh /usr/local/bin/plugins.sh  
COPY src/install-plugins.sh /usr/local/bin/install-plugins.sh  
  
# USER jenkins  
RUN install-plugins.sh git \  
github \  
docker \  
kubernetes \  
livescreenshot \  
google-cloud-backup \  
google-container-registry-auth \  
google-source-plugin \  
google-storage-plugin \  
gcloud-sdk \  
simple-theme-plugin  
  
EXPOSE 8080 50000  
RUN stat /var/jenkins_home  
ENTRYPOINT ["/usr/local/bin/jenkins.sh"]

