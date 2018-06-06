FROM seeruk/jenkins-slave:latest  
MAINTAINER Elliot Wright <hello@elliotdwright.com>  
  
COPY provisioning/00-docker-group.sh /opt/jenkins-slave-
setup/provisioning/00-docker-group.sh  
  
ENV DOCKER_VERSION 17.05  
ENV DOCKER_COMPOSE_VERSION 1.15.0  
RUN set -x \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys \  
"58118E89F3A912897C070ADBF76221572C52609D" \  
&& echo "deb http://apt.dockerproject.org/repo ubuntu-xenial main" >
/etc/apt/sources.list.d/docker.list \  
&& apt-get update \  
&& apt-get install -y curl docker-engine=${DOCKER_VERSION}.* \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& chmod +x /opt/jenkins-slave-setup/provisioning/00-docker-group.sh  
  
WORKDIR /opt/jenkins-slave-setup  
  
ENTRYPOINT ["/opt/jenkins-slave-setup/docker-entrypoint.sh"]  
  
CMD ["/opt/jenkins-slave-setup/start-slave.sh"]  

