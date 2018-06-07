FROM usgsastro/centos7  
  
  
ENV SWARM_CLIENT_VERSION="3.3" \  
DOCKER_COMPOSE_VERSION="1.16.1" \  
COMMAND_OPTIONS="" \  
DOCKER_HOST="" \  
DOCKER_TLS_VERIFY=""  
RUN adduser -G root -m jenkins && \  
wget -O /etc/yum.repos.d/docker.repo
https://download.docker.com/linux/centos/docker-ce.repo && \  
yum update -y && yum -y install java-1.8.0-openjdk python docker-ce && \  
wget --no-check-certificate -P /home/jenkins/ https://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-
client/${SWARM_CLIENT_VERSION}/swarm-client-${SWARM_CLIENT_VERSION}.jar && \  
wget --no-check-certificate -O /usr/local/bin/docker-compose
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-Linux-x86_64 && \  
chmod a+x /usr/local/bin/docker-compose  
  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  

