FROM openjdk:8-jdk  
  
RUN apt-get update && apt-get install -y git curl && rm -rf
/var/lib/apt/lists/*  
  
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
# removed so all data is contained in the image and not mapped to the file
system.  
#VOLUME /var/jenkins_home  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
ENV TINI_VERSION 0.9.0  
ENV TINI_SHA fa23d1e20732501c3bb8eeeca423c89ac80ed452  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fsSL
https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-static
-o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha1sum -c -  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
  
# jenkins version being bundled in this docker image  
ARG JENKINS_VERSION  
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.19.1}  
  
# jenkins.war checksum, download will be validated using it  
ARG JENKINS_SHA=dc28b91e553c1cd42cc30bd75d0f651671e6de0b  
  
# Can be used to customize where jenkins.war get downloaded from  
ARG JENKINS_URL=http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-
war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war  
  
# could use ADD but this one does not check Last-Modified header neither does
it allow to control checksum  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fsSL ${JENKINS_URL} -o /usr/share/jenkins/jenkins.war \  
&& echo "${JENKINS_SHA} /usr/share/jenkins/jenkins.war" | sha1sum -c -  
  
ENV JENKINS_UC https://updates.jenkins.io  
RUN chown -R ${user} "$JENKINS_HOME" /usr/share/jenkins/ref  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
USER ${user}  
  
COPY jenkins-support /usr/local/bin/jenkins-support  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  
ENV BASE_URL http://flynnshome.com/downloads  
ENV JENKINS_ALI "$BASE_URL"/ALI29/agents/build-integration/jenkins  
  
# plugins needed from HPE  
ENV OCTANE_JENKINS_CI hp-lifecycle-management-ci-plugin  
ENV ALI_GIT ali-jenkins-git-plugin  
ENV ALI ali-jenkins-plugin  
  
#NOTE had to change the endings from .hpi to .bin to store on webserver  
# so they would be pulled down. not sure why but then changed back to .hpi  
# for use by Jenkins.  
ADD "$BASE_URL"/octane/"$OCTANE_JENKINS_CI".12.53.12.bin
"$JENKINS_HOME"/plugins/"$OCTANE_JENKINS_CI".hpi  
ADD "$JENKINS_ALI"/"$ALI".bin "$JENKINS_HOME"/plugins/"$ALI".hpi  
#ADD "$JENKINS_ALI"/"$ALI_GIT".bin "$JENKINS_HOME"/plugins/"$ALI_GIT".hpi  
# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY install-plugins.sh /usr/local/bin/install-plugins.sh  
RUN /usr/local/bin/install-plugins.sh \  
async-http-client:1.7.24.1 \  
cvs:2.12 \  
depgraph-view:0.11 \  
hp-application-automation-tools-plugin:4.5.0 \  
git-tag-message:1.5 \  
github-oauth:0.24 \  
github-pullrequest:0.1.0-rc9 \  
gitlab-oauth:1.0.9 \  
gradle:1.25 \  
greenballs:1.15 \  
jenkins-multijob-plugin:1.23 \  
jquery:1.11.2-0 \  
jquery-ui:1.0.2 \  
maven-release-cascade:1.3.2 \  
maven-plugin:2.14 \  
m2release:0.14.0 \  
nunit:0.18 \  
repository:1.3  

