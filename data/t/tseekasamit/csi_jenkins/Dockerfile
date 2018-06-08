FROM openjdk:8-jdk  
  
MAINTAINER Teerawit S.  
ENV LC_ALL C.UTF-8  
#RUN apt-get update && apt-get install -y git curl && rm -rf
/var/lib/apt/lists/*  
#ENV http_proxy http://webproxy.int.westgroup.com:80  
#ENV https_proxy http://webproxy.int.westgroup.com:80  
RUN apt-get update; apt-get -y upgrade; apt-get install -y lftp curl wget
dstat dnsutils rlwrap libaio-dev ruby rubygems  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
ARG user=gscadmin  
ARG group=gscadmin  
ARG uid=69192  
ARG gid=69192  
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
  
ENV TINI_VERSION 0.14.0  
ENV TINI_SHA 6c41ec7d33e857d4779f14d9c74924cab0c7973485d2972419a3b7c7620ff5fd  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fsSL
https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-
static-amd64 -o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha256sum -c -  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
  
# jenkins version being bundled in this docker image  
ARG JENKINS_VERSION  
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.46.3}  
  
# jenkins.war checksum, download will be validated using it  
ARG
JENKINS_SHA=00424d3c851298b29376d1d09d7d3578a2bc4a03acf3914b317c47707cd5739a  
  
# Can be used to customize where jenkins.war get downloaded from  
ARG JENKINS_URL=https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war  
  
# could use ADD but this one does not check Last-Modified header neither does
it allow to control checksum  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fsSL ${JENKINS_URL} -o /usr/share/jenkins/jenkins.war \  
&& echo "${JENKINS_SHA} /usr/share/jenkins/jenkins.war" | sha256sum -c -  
  
ENV JENKINS_UC https://updates.jenkins.io  
RUN chown -R ${user} "$JENKINS_HOME" /usr/share/jenkins/ref  
  
#Kettle  
RUN mkdir -p /var/kettle_home  
RUN wget
https://sourceforge.net/projects/pentaho/files/Data%20Integration/7.1/pdi-
ce-7.1.0.0-12.zip -P /var/kettle_home  
RUN chown -R ${user}:${user} /var/kettle_home  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
#RUN unzip pdi-ce-7.1.0.0-12.zip -d kettle  
USER ${user}  
  
COPY jenkins-support /usr/local/bin/jenkins-support  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  
# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY install-plugins.sh /usr/local/bin/install-plugins.sh  
  
#ENV _PENTAHO_JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-amd64  
#EnV _PENTAHO_JAVA /usr/lib/jvm/java-1.8.0-openjdk-amd64/jre/lib  

