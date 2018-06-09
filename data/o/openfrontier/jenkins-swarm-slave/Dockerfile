FROM openjdk:8-jdk-alpine  
  
MAINTAINER zsx <thinkernel@gmail.com>  
  
ENV JENKINS_SWARM_VERSION 3.9  
ENV JENKINS_SWARM_DOWNLOAD_SITE https://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-client  
ENV JENKINS_HOME /home/jenkins  
ENV JENKINS_USER jenkins  
  
RUN set -x &&\  
apk add --update --no-cache curl bash openssh git  
  
RUN adduser -D -h "${JENKINS_HOME}" -g "Jenkins User" -s /sbin/nologin
"${JENKINS_USER}"  
RUN curl --create-dirs -sSLo /usr/share/jenkins/swarm-
client-${JENKINS_SWARM_VERSION}.jar \  
${JENKINS_SWARM_DOWNLOAD_SITE}/${JENKINS_SWARM_VERSION}/swarm-
client-${JENKINS_SWARM_VERSION}.jar \  
&& chmod 755 /usr/share/jenkins  
  
COPY jenkins-slave.sh /usr/local/bin/jenkins-slave.sh  
  
RUN mkdir /docker-entrypoint-init.d  
ONBUILD ADD ./*.sh /docker-entrypoint-init.d/  
  
USER "${JENKINS_USER}"  
ENTRYPOINT ["/usr/local/bin/jenkins-slave.sh"]  

