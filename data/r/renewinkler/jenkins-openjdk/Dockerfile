FROM openjdk:8  
ENV DOCKER_VERSION 1.12.0  
ENV DOCKER_COMPOSE_VERSION 1.8.0  
ENV DOCKER_MACHINE_VERSION 0.8.0  
# Tools  
RUN apt-get update -qq && apt-get install -qq curl wget git subversion nano
nodejs npm iputils-ping && apt-get clean  
  
# Maven  
RUN curl -sf -o /opt/apache-maven-bin.tar.gz
http://archive.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz; \  
tar xzf /opt/apache-maven-bin.tar.gz -C /opt/; \  
rm /opt/apache-maven-bin.tar.gz; \  
ln -s /opt/apache-maven-3.3.9 /opt/maven  
ENV MAVEN_HOME /opt/maven  
  
# Docker bins  
WORKDIR /home/toolbox/  
RUN curl -L -o /tmp/docker-latest.tgz
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz && \  
tar -xvzf /tmp/docker-latest.tgz && \  
mv docker/* /usr/bin/  
  
# Docker compose  
RUN curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
# Docker machine  
RUN curl -L
https://github.com/docker/machine/releases/download/v${DOCKER_MACHINE_VERSION}/docker-
machine-`uname -s`-`uname -m` > /usr/local/bin/docker-machine && \  
chmod +x /usr/local/bin/docker-machine  
  
# Jenkins  
ENV JENKINS_HOME /opt/jenkins  
ENV JENKINS_MIRROR http://mirrors.jenkins-ci.org  
RUN mkdir -p $JENKINS_HOME  
RUN curl -sf -o /opt/jenkins/jenkins.war -L
$JENKINS_MIRROR/war/latest/jenkins.war  
RUN mkdir -p $JENKINS_HOME/plugins; for plugin in greenballs; \  
do curl -sf -o $JENKINS_HOME/plugins/${plugin}.hpi -L
$JENKINS_MIRROR/plugins/${plugin}/latest/${plugin}.hpi; done  
VOLUME $JENKINS_HOME/data  
WORKDIR $JENKINS_HOME  
  
EXPOSE 8080  
HEALTHCHECK \--interval=20s --timeout=10s CMD curl --fail
http://localhost:8080/ || exit 1  
CMD [ "java", "-jar", "jenkins.war" ]  
  

