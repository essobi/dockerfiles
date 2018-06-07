FROM ubuntu:16.04  
# Docker binaries versions.  
ENV DOCKER_VERSION=1.12.2 \  
DOCKER_COMPOSE_VERSION=1.8.1 \  
# Group ID and Name for host's docker user.  
# Note: 999 is gid on AWS.  
# TODO: Make it configurable or autodetect.  
DOCKER_GID=999 \  
DOCKER_GROUP=docker \  
# Jenkins home dir.  
JENKINS_HOME_DIR=/home/jenkins  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
# Install essential tools.  
git \  
wget \  
curl \  
sudo \  
# JDK 7 (latest edition).  
default-jdk && \  
# Apt cleanup.  
apt-get -q autoremove && apt-get -q clean -y && rm -rf /var/lib/apt/lists/* &&
rm -f /var/cache/apt/*.bin && \  
# Install Docker CLI, Docker Compose and Docksal fin.  
curl -sSL "https://get.docker.com/builds/$(uname -s)/$(uname
-m)/docker-${DOCKER_VERSION}.tgz" | tar zxf - --strip-components 1 -C
/usr/local/bin docker/docker && \  
curl -sSL
"https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \  
# TODO: Fin binary may depend on a specific docker version.  
curl -sSL "https://raw.githubusercontent.com/docksal/docksal/develop/bin/fin"
-o /usr/local/bin/fin && \  
chmod +x /usr/local/bin/* && \  
# Create Docker user group.  
groupadd -g ${DOCKER_GID} ${DOCKER_GROUP} && \  
# Create jenkins user in docker group.  
useradd -g users -G ${DOCKER_GROUP} -m -d ${JENKINS_HOME_DIR} -s /bin/sh
jenkins && \  
# Set jennkins user password.  
echo "jenkins:jenkins" | chpasswd && \  
# Add the jenkins user to sudoers.  
echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
# Create docksal and jenkins working dirs.  
mkdir -p ${JENKINS_HOME_DIR}/.docksal && \  
mkdir -p ${JENKINS_HOME_DIR}/.jenkins && \  
# Set jenkins owner for sure.  
chown -R jenkins:docker ${JENKINS_HOME_DIR} && \  
# Set DNS.  
echo "nameserver 8.8.8.8\nnameserver 8.8.4.4\n" > /etc/resolv.conf  

