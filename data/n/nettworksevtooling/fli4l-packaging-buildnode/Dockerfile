FROM nettworksevtooling/fli4l-packaging-container:latest  
MAINTAINER Yves Schumann <yves@eisfair.org>  
  
# Configuration for Jenkins swarm  
# Default values for potential build time parameters  
ARG JENKINS_IP="localhost"  
ARG JENKINS_TUNNEL=""  
ARG USERNAME="admin"  
ARG PASSWORD="admin"  
ARG DESCRIPTION="Swarm node for fli4l-packaging"  
ARG LABELS="linux swarm fli4l-packaging"  
ARG NAME="fli4l-packaging"  
ARG UID="1058"  
ARG GID="1007"  
# Environment variables for swarm client  
ENV JENKINS_URL=http://$JENKINS_IP \  
JENKINS_TUNNEL=$JENKINS_TUNNEL \  
JENKINS_USERNAME=$USERNAME \  
JENKINS_PASSWORD=$PASSWORD \  
EXECUTORS=1 \  
DESCRIPTION=$DESCRIPTION \  
LABELS=$LABELS \  
NAME=$NAME \  
SWARM_PLUGIN_VERSION=3.7 \  
WORK_DIR=/data/work \  
SHARED_DIR=/data/shared/fli4l  
  
# Setup jenkins account  
# Create working directory  
# Change user UID and GID  
RUN groupadd --gid ${GID} fleis \  
&& useradd --create-home --home-dir /home/jenkins --shell /bin/bash --uid
${UID} \--gid ${GID} jenkins \  
&& echo "jenkins:jenkins" | chpasswd \  
&& chown jenkins:fleis /home/jenkins -R \  
&& ulimit -v unlimited  
  
RUN apt-get autoremove \  
&& apt-get clean \  
&& apt-get update \  
&& apt-get install -y \  
default-jdk  
  
# Mount point for Jenkins .ssh folder  
VOLUME /home/jenkins/.ssh  
  
# Install swarm client  
ADD "https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/${SWARM_PLUGIN_VERSION}/swarm-client-${SWARM_PLUGIN_VERSION}.jar"
/data/swarm-client.jar  
  
# Link ~/.fbr to shared location and update ownership  
RUN mkdir -p ${SHARED_DIR}/.fbr \  
&& ln -s ${SHARED_DIR}/.fbr /home/jenkins/.fbr \  
&& chown -R jenkins:fleis /data  
  
# Switch to user jenkins  
USER jenkins  
  
# Start ssh  
#CMD ["/usr/sbin/sshd", "-D"]  
  
CMD java \  
-jar /data/swarm-client.jar \  
-executors "${EXECUTORS}" \  
-noRetryAfterConnected \  
-description "${DESCRIPTION}" \  
-fsroot "${WORK_DIR}" \  
-master "${JENKINS_URL}" \  
-tunnel "${JENKINS_TUNNEL}" \  
-username "${JENKINS_USERNAME}" \  
-password "${JENKINS_PASSWORD}" \  
-labels "${LABELS}" \  
-name "${NAME}" \  
-sslFingerprints " "  

