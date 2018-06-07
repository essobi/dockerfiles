FROM nettworksevtooling/eisfair-ng-buildcontainer:3.7-x86-latest  
MAINTAINER Yves Schumann <yves@eisfair.org>  
  
# Configuration for Jenkins swarm  
# Default values for potential build time parameters  
ARG JENKINS_IP="localhost"  
ARG JENKINS_TUNNEL=""  
ARG USERNAME="admin"  
ARG PASSWORD="admin"  
ARG DESCRIPTION="Swarm node with eisfair-ng sdk (v3.7)"  
ARG LABELS="linux swarm e-ng-v3.7"  
ARG NAME="e-ng-v3.7"  
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
WORK_DIR=/data/work  
  
# Setup jenkins account  
# Create working directory  
# Change user UID and GID  
RUN addgroup -g ${GID} jenkins \  
&& adduser -D -h /home/jenkins -u ${UID} -G jenkins -s /bin/bash jenkins \  
&& addgroup jenkins abuild \  
&& echo "jenkins:jenkins" | chpasswd \  
&& echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \  
&& chown jenkins:jenkins /home/jenkins -R  
  
# Install OpenJDK  
RUN apk add openjdk8  
  
# Mount point for Jenkins .ssh folder  
VOLUME /home/jenkins/.ssh  
  
# Install swarm client  
ADD "https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/${SWARM_PLUGIN_VERSION}/swarm-client-${SWARM_PLUGIN_VERSION}.jar"
/data/swarm-client.jar  
RUN chown -R jenkins:jenkins /data  
  
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

