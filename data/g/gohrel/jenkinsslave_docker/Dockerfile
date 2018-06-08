############################################################  
# Dockerfile to build jenkins swarm slaves container images that can build and
publish new docker images  
# Based on debian:buster  
############################################################  
  
FROM debian:buster  
  
MAINTAINER Holger Zunker <holger50@gmx.de>  
  
# Create a non-root user  
RUN useradd -m user  
WORKDIR /home/user  
  
#Install docker  
USER root  
RUN apt-get update  
RUN apt-get install curl apt-utils apt-transport-https ca-certificates gnupg2
software-properties-common -y  
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add -  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable"  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install docker-ce -y  
  
#Install Jenkins dependencies  
ENV JENKINS_MASTER_USERNAME="jenkins" \  
JENKINS_MASTER_PASSWORD="jenkins" \  
JENKINS_MASTER_URL="http://jenkins:8080/" \  
JENKINS_SLAVE_MODE="exclusive" \  
JENKINS_SLAVE_NAME="swarm-$RANDOM" \  
JENKINS_SLAVE_WORKERS="1" \  
JENKINS_SLAVE_LABELS="" \  
AVD=""  
ENV JENKINS_SLAVE_ROOT="/home/user/"  
ENV HOME=/home/jenkins-slave \  
JENKINS_SWARM_VERSION=3.8 \  
JENKINS_SWARM_JAR_PATH=/home/user  
ENV JENKINS_SWARM_JAR=${JENKINS_SWARM_JAR_PATH}/swarm.jar  
COPY scripts/entrypoint.sh /home/user/scripts/  
  
RUN mkdir -p "$JENKINS_SLAVE_ROOT"  
# Install Jenkins slave (swarm)  
RUN mkdir -p $JENKINS_SWARM_JAR_PATH \  
&& chmod 755 $JENKINS_SWARM_JAR_PATH \  
&& curl -SLo $JENKINS_SWARM_JAR http://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-
client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION.jar  
  
USER root  
RUN chmod +x /home/user/scripts/entrypoint.sh  
RUN chown -R user:user /home/user/scripts/*  
ENTRYPOINT /home/user/scripts/entrypoint.sh  
  
USER user  
VOLUME ${HOME}  
WORKDIR ${HOME}  
  
  
  
  
  

