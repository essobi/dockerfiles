FROM ubuntu:xenial  
MAINTAINER maintainer  
ENV TERM=linux  
  
# remove openjdk  
RUN apt remove -y openjdk*  
  
# install docker  
RUN apt-get update && \  
apt-get install -y git wget apt-transport-https ca-certificates  
  
RUN apt-key adv \  
\--keyserver hkp://ha.pool.sks-keyservers.net:80 \  
\--recv-keys 58118E89F3A912897C070ADBF76221572C52609D  
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | tee
/etc/apt/sources.list.d/docker.list  
RUN apt-get update && \  
apt-get install -y docker-engine  
  
# install docker-compose  
ENV DOCKER_COMPOSE_VERSION=1.8.1  
ENV DOCKER_COMPOSE_DIR=/opt/docker-compose  
  
RUN mkdir -p ${DOCKER_COMPOSE_DIR} && \  
wget
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-$(uname -s)-$(uname -m) \  
\--output-document=${DOCKER_COMPOSE_DIR}/docker-compose && \  
chmod +x ${DOCKER_COMPOSE_DIR}/docker-compose && \  
ln -s ${DOCKER_COMPOSE_DIR}/docker-compose /usr/bin/docker-compose  
  
# Install Oracle JDK 8  
ENV JDK_URL=http://download.oracle.com/otn-
pub/java/jdk/8u112-b15/jdk-8u112-linux-x64.tar.gz  
ENV JDK_TGZ=jdk-8u112-linux-x64.tar.gz  
ENV JDK_DIR=jdk1.8.0_112  
ENV JDK_PATH=/opt/jdk  
  
RUN wget --no-check-certificate --header "Cookie: oraclelicense=accept-
securebackup-cookie" \  
${JDK_URL} && \  
mkdir ${JDK_PATH} && \  
tar -zxf ${JDK_TGZ} -C ${JDK_PATH} && \  
rm ${JDK_TGZ} && \  
update-alternatives --install /usr/bin/java java
${JDK_PATH}/${JDK_DIR}/bin/java 100 && \  
update-alternatives --install /usr/bin/javac javac
${JDK_PATH}/${JDK_DIR}/bin/javac 100 && \  
update-alternatives --install /usr/bin/jar jar ${JDK_PATH}/${JDK_DIR}/bin/jar
100 && \  
ln -s ${JDK_PATH}/${JDK_DIR} ${JDK_PATH}/latest  
  
# Install maven  
ENV MVN_VERSION=3.3.9  
ENV
MVN_URL=http://mirrors.sonic.net/apache/maven/maven-3/${MVN_VERSION}/binaries/apache-
maven-${MVN_VERSION}-bin.tar.gz  
ENV MVN_PATH=/opt/maven  
ENV MVN_DIR=apache-maven-${MVN_VERSION}  
  
RUN wget ${MVN_URL} && \  
mkdir ${MVN_PATH} && \  
tar -zxf apache-maven-${MVN_VERSION}-bin.tar.gz -C ${MVN_PATH} && \  
rm -f apache-maven-${MVN_VERSION}-bin.tar.gz && \  
ln -s ${MVN_PATH}/${MVN_DIR}/bin/mvn /usr/bin/mvn && \  
ln -s ${MVN_PATH}/${MVN_DIR} ${MVN_PATH}/latest  
  
# Install Jenkins Swarm  
ENV SWARM_PATH=/opt/jenkins  
ENV JENKINS_SWARM_VERSION=2.2  
ENV JENKINS_SWARM_JAR=swarm-client-${JENKINS_SWARM_VERSION}-jar-with-
dependencies.jar  
ENV JENKINS_SWARM_URL=http://repo.jenkins-ci.org/releases/org/jenkins-
ci/plugins/swarm-client/${JENKINS_SWARM_VERSION}/swarm-
client-${JENKINS_SWARM_VERSION}-jar-with-dependencies.jar  
  
RUN mkdir -p ${SWARM_PATH} && \  
wget --no-check-certificate --output-
document=${SWARM_PATH}/${JENKINS_SWARM_JAR} ${JENKINS_SWARM_URL}  
  
# Run jenkins slave  
# $ docker inspect --format='{{.Config.Hostname}}' jenkins  
ENV SWARM_CMD_MASTER_HOST="jenkins.master"  
ENV SWARM_CMD_MASTER_PORT=8080  
ENV
SWARM_CMD_MASTER_URL="http://${SWARM_CMD_MASTER_HOST}:${SWARM_CMD_MASTER_PORT}"  
ENV SWARM_CMD_NAME="maven.swarm.slave"  
ENV SWARM_CMD_LABELS="maven"  
ENV SWARM_CMD_USERNAME="jenkins_user"  
ENV SWARM_CMD_PASSWORD="jenkins_user_password"  
CMD [ "/bin/bash", "-c", \  
"java -jar ${SWARM_PATH}/${JENKINS_SWARM_JAR} -master ${SWARM_CMD_MASTER_URL}
-name ${SWARM_CMD_NAME} -labels ${SWARM_CMD_LABELS} -username
${SWARM_CMD_USERNAME} -password ${SWARM_CMD_PASSWORD}" \  
]  

