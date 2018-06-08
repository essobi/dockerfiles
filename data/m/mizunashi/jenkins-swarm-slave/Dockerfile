FROM java:latest  
MAINTAINER Mizunashi Mana <mizunashi_mana@mma.club.uec.ac.jp>  
  
RUN apt-get update \  
&& apt-get install -y sudo curl \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV JENKINS_WORKUSER="jenkins" \  
JENKINS_WORKSPACE="/var/jenkins_ws" \  
SETUP_DIR="/var/cache/jenkins_ws"  
ENV JENKINS_SWARM_VERSION=1.24  
RUN useradd -c "Jenkins Slave user" -d "${JENKINS_WORKSPACE}" \  
-u 1000 -m -s /bin/bash ${JENKINS_WORKUSER}  
  
RUN mkdir -p ${SETUP_DIR}  
RUN curl -fL http://maven.jenkins-
ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-
client/${JENKINS_SWARM_VERSION}/swarm-client-${JENKINS_SWARM_VERSION}-jar-
with-dependencies.jar \  
-o ${SETUP_DIR}/swarm-client-${JENKINS_SWARM_VERSION}-jar-with-dependencies.jar  
RUN curl -fL http://maven.jenkins-
ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-
client/${JENKINS_SWARM_VERSION}/swarm-client-${JENKINS_SWARM_VERSION}-jar-
with-dependencies.jar.sha1 \  
-o ${SETUP_DIR}/swarm-client-${JENKINS_SWARM_VERSION}-jar-with-dependencies.jar.sha1 \  
&& echo "`cat ${SETUP_DIR}/swarm-client-${JENKINS_SWARM_VERSION}-jar-with-
dependencies.jar.sha1` ${SETUP_DIR}/swarm-client-${JENKINS_SWARM_VERSION}-jar-
with-dependencies.jar" | sha1sum -c -  
RUN chmod 755 ${SETUP_DIR}  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
USER ${JENKINS_WORKUSER}  
VOLUME ["${JENKINS_WORKSPACE}"]  
WORKDIR ${JENKINS_WORKSPACE}  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

