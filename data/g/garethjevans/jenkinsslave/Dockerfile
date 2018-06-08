FROM openjdk:8-jdk-alpine  
  
RUN apk add --no-cache git openssh-client wget curl unzip bash ttf-dejavu
coreutils  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
# Jenkins is run with user `jenkins`, uid = 1000  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
RUN addgroup -g ${gid} ${group} \  
&& adduser -h /home/jenkins -u ${uid} -G ${group} -s /bin/bash -D ${user}  
  
ENV JENKINS_SWARM_VERSION 3.6  
RUN curl --create-dirs -sSLo /usr/share/jenkins/swarm-client.jar
http://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/${JENKINS_SWARM_VERSION}/swarm-client-${JENKINS_SWARM_VERSION}.jar && \  
chmod 755 /usr/share/jenkins  
  
RUN mkdir /opt  
  
# RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
COPY swarm/slave.sh /home/jenkins/slave.sh  
RUN chmod +x /home/jenkins/slave.sh  
  
ENTRYPOINT ["/home/jenkins/slave.sh"]  

