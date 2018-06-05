FROM debian:jessie  
  
MAINTAINER Camille Meulien <camille.meulien@gmail.com>  
  
#  
# Jenkins slave install  
#  
ENV HOME=/home/jenkins-slave \  
JENKINS_SWARM_VERSION=2.2 \  
JENKINS_SWARM_JAR=/usr/share/jenkins/swarm-client-2.2-jar-with-
dependencies.jar  
  
RUN apt-get update \  
&& set -x \  
&& apt-get install -y curl \  
&& useradd -d ${HOME} -m jenkins-slave \  
&& mkdir -p /usr/share/jenkins \  
&& chmod 755 /usr/share/jenkins \  
&& curl -sSLo ${JENKINS_SWARM_JAR} http://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-
client/${JENKINS_SWARM_VERSION}/swarm-client-${JENKINS_SWARM_VERSION}-jar-
with-dependencies.jar  
  
RUN env | grep -E "(JENKINS|JAVA)" > /etc/docker.properties  
  
COPY entrypoint.sh /  
RUN chmod 755 /entrypoint.sh \  
&& chown root:root /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
#  
# Docker install  
#  
RUN apt-get install -y openjdk-7-jre-headless apt-transport-https ca-
certificates \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo deb https://apt.dockerproject.org/repo debian-jessie main >
/etc/apt/sources.list.d/docker.list \  
&& apt-get update  
  
RUN apt-get install -y docker-engine=$(apt-cache show docker-engine | grep -F
"Version: 1.12" | sort | tail -n1 | sed -r 's/Version: //')  
  
USER jenkins-slave  
  
VOLUME $HOME  

