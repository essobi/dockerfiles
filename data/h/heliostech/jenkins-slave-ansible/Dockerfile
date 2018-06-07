FROM centos:centos7  
  
MAINTAINER Camille Meulien <camille.meulien@gmail.com>  
  
#  
# Ansible and misc tools setup  
#  
RUN yum install -y \  
ansible \  
epel-release \  
git \  
wget;  
  
#  
# Jenkins Slave setup  
#  
ENV HOME=/home/jenkins-slave \  
JENKINS_SWARM_VERSION=2.2 \  
JENKINS_SWARM_JAR_PATH=/usr/share/jenkins  
ENV JENKINS_SWARM_JAR=$JENKINS_SWARM_JAR_PATH/swarm-
client-${JENKINS_SWARM_VERSION}-jar-with-dependencies.jar  
  
RUN yum install -y java-1.8.0-openjdk-headless \  
&& useradd -d $HOME -m jenkins-slave \  
&& mkdir -p $JENKINS_SWARM_JAR_PATH \  
&& chmod 755 $JENKINS_SWARM_JAR_PATH \  
&& curl -sSLo $JENKINS_SWARM_JAR https://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-
client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION-jar-with-
dependencies.jar \  
&& JENKINS_SWARM_JAR_SHA1=$(curl -s https://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-
client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION-jar-with-
dependencies.jar.sha1) \  
&& echo "${JENKINS_SWARM_JAR_SHA1} ${JENKINS_SWARM_JAR}" | sha1sum -c -  
  
COPY entrypoint.sh /  
RUN chmod 755 /entrypoint.sh \  
&& chown root:root /entrypoint.sh  
  
USER jenkins-slave  
VOLUME $HOME  
  
ENTRYPOINT ["/entrypoint.sh"]  

