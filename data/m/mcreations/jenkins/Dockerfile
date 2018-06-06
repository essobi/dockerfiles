## -*- docker-image-name: "mcreations/jenkins" -*-  
FROM mcreations/openwrt-java:jdk8  
MAINTAINER Reza Rahimi <rahimi@m-creations.net>  
  
RUN opkg update && opkg install \  
coreutils-base64 \  
coreutils-nohup \  
coreutils-sha1sum \  
coreutils-sha256sum \  
curl \  
git \  
git-http \  
graphviz \  
libltdl \  
openssh-client \  
openssl-util \  
shadow-groupadd \  
shadow-groupmod \  
shadow-su \  
shadow-useradd \  
shadow-usermod \  
zip \  
&& dot -c  
  
ENV JENKINS_HOME /data/jenkins_home  
ENV HOME /data/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
# the group ID of the docker group on the Docker host (for the permissions of
the docker unix domain socket)  
ENV DOCKER_HOST_GID 131  
ENV JENKINS_UID 201  
ENV JENKINS_GID 201  
# Jenkins is run with user `jenkins`  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
RUN groupadd -g ${JENKINS_GID} jenkins \  
&& groupadd -g ${DOCKER_HOST_GID} docker \  
&& mkdir -p ${JENKINS_HOME} \  
&& useradd -d "$JENKINS_HOME" -u ${JENKINS_UID} -g ${JENKINS_GID} -G docker -m
-s /bin/bash jenkins \  
&& chown -R jenkins:root /data \  
&& chown -R jenkins:jenkins "${JENKINS_HOME}"  
  
# Jenkins home directory is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME /data  
  
ENV SSL_CERTIFICATES_HOME /data/ssl  
ENV SSL_CERTIFICATES_DEST_HOME /etc/ssl/certs  
ENV JAVA_SECURITY_KEYSTORE_HOME $SSL_CERTIFICATES_HOME/keystore  
ENV JAVA_SECURITY_KEYSTORE_PATH $JAVA_SECURITY_KEYSTORE_HOME/cacerts  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
ENV TINI_VERSION 0.13.2  
ENV TINI_SHA afbf8de8a63ce8e4f18cb3f34dfdbbd354af68a1  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fsSL
https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-
static-amd64 -o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha1sum -c -  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
  
# jenkins version being bundled in this docker image  
ARG JENKINS_VERSION  
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.46.1}  
  
# jenkins.war checksum, download will be validated using it  
ARG
JENKINS_SHA=33a3f4d983c6188a332291e1d974afa0a2ee96a0ae3cb6dd4f2098086525f9f1  
  
# Can be used to customize where jenkins.war get downloaded from  
ARG JENKINS_URL=https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war  
  
# could use ADD but this one does not check Last-Modified header neither does
it allow to control checksum  
# see https://github.com/docker/docker/issues/8331  
RUN wget --progress=dot:giga ${JENKINS_URL} -O /usr/share/jenkins/jenkins.war
\  
&& echo "${JENKINS_SHA} /usr/share/jenkins/jenkins.war" | sha256sum -c -  
  
ENV MAVEN_MAJOR_VERSION 3  
ENV MAVEN_VERSION 3.3.9  
ENV MAVEN_HOME /opt/maven  
ENV MAVEN_DOWNLOAD_URL http://ftp.halifax.rwth-
aachen.de/apache/maven/maven-${MAVEN_MAJOR_VERSION}/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz  
ENV MAVEN_REPO /data/jenkins_home/maven-repository  
  
ENV JENKINS_UC https://updates.jenkins.io  
RUN mkdir -p $JENKINS_HOME \  
&& mkdir -p $SSL_CERTIFICATES_HOME \  
&& wget -O /tmp/maven.tgz --progress=dot:giga $MAVEN_DOWNLOAD_URL \  
&& cd /tmp/ \  
&& tar -xvzf maven.tgz \  
&& mv /tmp/apache-maven-${MAVEN_VERSION} $MAVEN_HOME \  
&& rm -f /tmp/maven.tgz \  
&& chown -R jenkins:jenkins "${JENKINS_HOME}" /usr/share/jenkins/ref \  
&& sed -i
"s#\\(</settings>\\)#<localRepository>${MAVEN_REPO}</localRepository>\n\1#g"
$MAVEN_HOME/conf/settings.xml \  
&& chown -R jenkins:root /data \  
&& chown -R jenkins:root "$JAVA_HOME" \  
&& chmod 775 "$SSL_CERTIFICATES_DEST_HOME"  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
COPY jenkins-support /usr/local/bin/jenkins-support  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
  
COPY start-jenkins /  
COPY jenkins-chown-and-start /  
  
CMD ["/jenkins-chown-and-start"]  
  
# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY install-plugins.sh /usr/local/bin/install-plugins.sh  
  
WORKDIR ${JENKINS_HOME}  

