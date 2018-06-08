FROM openjdk:8u131-jre  
  
ENV JENKINS_SWARM_HOME=/var/jenkins_home  
ENV JENKINS_SWARM_VERSION=3.4  
ENV DOCKER_VERSION=17.09.0-ce  
ENV DOCKER_COMPOSE_VERSION=1.16.1  
  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
  
COPY cmd.sh /cmd.sh  
  
RUN BIN_DIR=/usr/local/bin &&\  
groupadd -g ${gid} ${group} &&\  
useradd -d "${JENKINS_SWARM_HOME}" -u ${uid} -g ${gid} -m -s /bin/bash ${user}
&&\  
chmod +x /cmd.sh &&\  
  
# Jenkins Swarm  
JENKINS_SWARM_FILE="swarm-client-${JENKINS_SWARM_VERSION}.jar" &&\  
JENKINS_SWARM_URL="https://repo.jenkins-ci.org/releases/org/jenkins-
ci/plugins/swarm-client/${JENKINS_SWARM_VERSION}/${JENKINS_SWARM_FILE}" &&\  
curl --create-dirs -fsSLo ${JENKINS_SWARM_HOME}/${JENKINS_SWARM_FILE}
"${JENKINS_SWARM_URL}" &&\  
chown -R ${user} ${JENKINS_SWARM_HOME} &&\  
  
# Docker  
DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz"
&&\  
curl -fsSL ${DOCKER_URL} | tar \--strip-components=1 -xz -C ${BIN_DIR} &&\  
  
# Docker Compose  
DOCKER_COMPOSE_URL="https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-Linux-x86_64" &&\  
curl -fsSLo ${BIN_DIR}/docker-compose ${DOCKER_COMPOSE_URL} &&\  
chmod +x ${BIN_DIR}/docker-compose  
  
WORKDIR ${JENKINS_SWARM_HOME}  
  
CMD /bin/bash /cmd.sh  

