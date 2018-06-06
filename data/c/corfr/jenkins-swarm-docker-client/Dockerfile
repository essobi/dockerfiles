FROM openjdk:8-jre  
  
MAINTAINER Bertrand Roussel <broussel@sierrawireless.com>  
  
# Release  
ENV JENKINS_SWARM_VERSION 3.4  
ENV SWARM_PLUGIN_URL https://repo.jenkins-ci.org/releases/org/jenkins-
ci/plugins/swarm-client/$JENKINS_SWARM_VERSION/swarm-
client-$JENKINS_SWARM_VERSION.jar  
  
# Snapshot  
ENV JENKINS_BUILD lastStableBuild  
ENV JENKINS_SWARM_VERSION 3.5-SNAPSHOT  
ENV SWARM_PLUGIN_URL https://jenkins.ci.cloudbees.com/job/plugins/job/swarm-
plugin/$JENKINS_BUILD/org.jenkins-ci.plugins\$swarm-
client/artifact/org.jenkins-ci.plugins/swarm-
client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION.jar  
  
# Dev build  
#ENV SWARM_PLUGIN_URL https://github.com/CoRfr/swarm-
plugin/releases/download/swarm-plugin-$JENKINS_SWARM_VERSION/swarm-client-jar-
with-dependencies.jar  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
ARG JENKINS_AGENT_HOME=/home/${user}  
  
# Docker version follows stable from CoreOS  
ENV DOCKER_VERSION 1.12.6  
RUN ( \  
groupadd -g ${gid} ${group} && \  
useradd -d "${JENKINS_AGENT_HOME}" -u "${uid}" -g "${gid}" -m -s /bin/bash
"${user}" )  
  
RUN ( \  
mkdir -p /usr/share/jenkins && \  
wget -O /usr/share/jenkins/swarm-client-$JENKINS_SWARM_VERSION-jar-with-
dependencies.jar $SWARM_PLUGIN_URL && \  
chmod -R 755 /usr/share/jenkins )  
  
COPY jenkins-slave.sh /usr/local/bin/jenkins-slave.sh  
  
RUN ( apt-get update && \  
apt-get -y install net-tools git python bzip2 jq netcat-openbsd && \  
rm -rf /var/lib/apt/lists/* )  
  
RUN ( cd /tmp && \  
curl -fsSLO
https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz && \  
tar --strip-components=1 -xvzf docker-$DOCKER_VERSION.tgz -C /usr/bin )  
  
# Provide docker group and make the executable accessible (ids from CoreOS &
Debian)  
RUN groupadd -g 233 docker  
RUN groupadd -g 999 docker2  
RUN usermod -a -G docker,docker2 "${user}"  
RUN chown root:docker /usr/bin/docker  
  
# bash as default shell  
RUN ( \  
echo "dash dash/sh boolean false" | debconf-set-selections && \  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash \  
)  
  
# Add Tini  
ENV TINI_VERSION v0.14.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-
static /opt/tini/tini  
RUN chmod +x /opt/tini/tini  
VOLUME /opt/tini  
ENTRYPOINT ["/opt/tini/tini", "--", "/usr/local/bin/jenkins-slave.sh"]  
  
# encaps  
RUN ( \  
cd /usr/bin && \  
wget https://github.com/swi-infra/jenkins-docker-encaps/archive/master.zip &&
\  
unzip master.zip && \  
mv jenkins-docker-encaps-master/encaps* . && \  
rm -rf master.zip jenkins-docker-encaps-master \  
)  
  
RUN chown -R ${uid}:${gid} ${JENKINS_AGENT_HOME}  
  
USER ${user}  
VOLUME ${JENKINS_AGENT_HOME}  
  

