FROM java:openjdk-7  
MAINTAINER "Franco Salonia" <franco.salonia@dinocloudconsulting.com>  
  
ENV MD5 15c1f0937b9b8dd3ceca8f2418801b54  
  
RUN mkdir -p /var/jenkins_home \  
&& useradd -d /var/jenkins_home/worker -u 1000 -m -s /bin/bash jenkins \  
&& curl -o /bin/swarm-client.jar -SL http://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-client/2.0/swarm-client-2.0-jar-
with-dependencies.jar \  
&& echo "$MD5 /bin/swarm-client.jar" | md5sum -c - \  
&& apt-get update \  
&& apt-get install --no-install-recommends bzip2 \  
&& rm -rf /var/lib/apt/lists/*  
  
# Used to set the docker group ID  
# Set to 497 by default, which is the group ID used by AWS Linux ECS Instance  
ARG DOCKER_GID=497  
ARG DOCKER_ENGINE=1.10.2  
ARG DOCKER_COMPOSE=1.6.2  
# Create Docker Group with GID  
# Set default value of 497 if DOCKER_GID set to blank string by Docker Compose  
RUN groupadd -g ${DOCKER_GID:-497} docker  
  
# Install Docker Engine  
RUN apt-get update -y && apt-get install apt-transport-https make gcc -y &&
apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" | tee
/etc/apt/sources.list.d/docker.list && \  
apt-get update -y && \  
apt-get purge lxc-docker* -y && \  
apt-get install docker-engine=${DOCKER_ENGINE:-1.10.2}-0~trusty -y && \  
usermod -aG docker jenkins && \  
usermod -aG users jenkins  
  
# Install Docker Compose  
RUN curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
COPY docker-entrypoint.sh /  
WORKDIR /var/jenkins_home/worker  
  
USER jenkins  
ENTRYPOINT ["bash", "/docker-entrypoint.sh"]  
CMD ["java", "-Xmx2048m", "-jar", "/bin/swarm-client.jar", "-fsroot",
"/var/jenkins_home/worker/"]  

