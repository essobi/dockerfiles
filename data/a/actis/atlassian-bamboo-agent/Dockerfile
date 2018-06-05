FROM centos:7  
MAINTAINER Gregory Nickonov <gregoryn@actis.ru>  
  
# Set Engine/Compose versions to be used  
ENV DOCKER_VERSION 17.06.2.ce  
ENV DOCKER_COMPOSE_VERSION 1.16.1  
ENV KUBECTL_VERSION 1.7.6  
LABEL com.digillect.components.docker.version="${DOCKER_VERSION}" \  
com.digillect.components.docker-compose.version="${DOCKER_COMPOSE_VERSION}" \  
com.digillect.components.kubectl.version="${KUBECTL_VERSION}"  
  
# Update system & install dependencies  
RUN yum -y update \  
&& yum -q -y install yum-utils device-mapper-persistent-data lvm2 \  
&& yum-config-manager --add-repo
https://download.docker.com/linux/centos/docker-ce.repo \  
&& yum -q -y install git java-1.8.0-openjdk-devel openssl unzip wget which
docker-ce-${DOCKER_VERSION} \  
&& yum -q -y clean all  
  
# Installing docker-compose  
RUN curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  
  
# Installing kubectl  
RUN curl -L https://storage.googleapis.com/kubernetes-
release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl >
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl  
  
# Preparing agent environment  
WORKDIR /root  
  
COPY bamboo-agent.sh /root/bamboo-agent.sh  
COPY bamboo-capabilities.properties /root/bamboo-capabilities.properties  
  
#USER bamboo-agent  
ENTRYPOINT ["/bin/bash", "-c", "/root/bamboo-agent.sh"]  

