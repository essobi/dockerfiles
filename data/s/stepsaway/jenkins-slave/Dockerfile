FROM java:8-jdk  
MAINTAINER StepsAway <devgru@stepsaway.com>  
  
ENV PACKAGES apparmor docker-engine git curl zip  
ENV RANCHER_COMPOSE v0.8.1  
ENV DOCKER_COMPOSE 1.7.1  
ENV JENKINS_SWARM_VERSION 2.1  
ENV HOME /home/jenkins-slave  
COPY cmd.sh /cmd.sh  
  
RUN apt-get update -qq && \  
apt-get upgrade -y && \  
apt-get install -y apt-transport-https ca-certificates && \  
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
echo deb https://apt.dockerproject.org/repo ubuntu-trusty main >
/etc/apt/sources.list.d/docker.list && \  
apt-get update && \  
apt-get install -y $PACKAGES && \  
curl -s -L
https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE/docker-
compose-Linux-x86_64 > /usr/local/bin/docker-compose && \  
curl -s -L https://github.com/rancher/rancher-
compose/releases/download/$RANCHER_COMPOSE/rancher-compose-linux-
amd64-$RANCHER_COMPOSE.tar.gz -o rancher-compose.tar.gz && \  
tar -zxvf rancher-compose.tar.gz -C /usr/local/bin/ && \  
rm rancher-compose.tar.gz && \  
chmod -R +x /usr/local/bin && \  
rm -rf /var/lib/apt/lists/* && \  
useradd -c "Jenkins Slave user" -d $HOME -m jenkins-slave && \  
chmod +x /cmd.sh && \  
curl --create-dirs -sSLo $HOME/swarm-client-$JENKINS_SWARM_VERSION-jar-with-
dependencies.jar http://maven.jenkins-
ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-
client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION-jar-with-
dependencies.jar  
  
CMD ["/cmd.sh"]  

