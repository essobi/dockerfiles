FROM maven:latest  
  
MAINTAINER Camille Meulien <camille.meulien@gmail.com>  
  
ENV HOME=/home/jenkins-slave \  
JENKINS_SWARM_VERSION=2.2 \  
JENKINS_SWARM_JAR_PATH=/usr/share/jenkins  
ENV JENKINS_SWARM_JAR=${JENKINS_SWARM_JAR_PATH}/swarm-
client-${JENKINS_SWARM_VERSION}-jar-with-dependencies.jar  
  
RUN useradd -d $HOME -m jenkins-slave \  
&& mkdir -p $JENKINS_SWARM_JAR_PATH \  
&& chmod 755 $JENKINS_SWARM_JAR_PATH \  
&& curl -sSLo $JENKINS_SWARM_JAR http://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-
client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION-jar-with-
dependencies.jar  
  
RUN env | grep -E "(JENKINS|JAVA)" > /etc/docker.properties  
  
COPY entrypoint.sh /usr/bin/  
RUN chmod 755 /usr/bin/entrypoint.sh  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
  
USER jenkins-slave  
VOLUME ${HOME}  
WORKDIR ${HOME}  

