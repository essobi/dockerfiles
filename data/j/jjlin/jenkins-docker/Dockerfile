FROM jenkins/jenkins:lts  
  
#  
# If no specific value is provided via `docker build --build-arg ...`,  
# then the latest released version is implied.  
#  
ARG DOCKER_VERSION  
ARG DOCKER_COMPOSE_VERSION  
  
ARG CURL="curl -fsSL"  
#  
# Values derived from
<https://github.com/jenkinsci/docker/blob/master/Dockerfile>.  
# `ENV JENKINS_HOME=...` is inherited, so it doesn't need to be redefined
here.  
#  
ARG JENKINS_USER="jenkins"  
#  
# Install Docker (client only) and Docker Compose.  
#  
# URLs to Docker static binary archives are taken from the `docker`
Dockerfiles.  
# See <https://hub.docker.com/_/docker/> for links to these Dockerfiles.  
#  
USER root  
COPY *.sh /usr/local/bin/  
RUN docker_version=${DOCKER_VERSION:-$(get-latest-docker-release.sh edge)} \  
&& docker_compose_version=${DOCKER_COMPOSE_VERSION:-$(get-latest-release-
tag.sh docker compose)} \  
&& echo "Versions" \  
&& echo "========" \  
&& echo "Docker: ${docker_version}" \  
&& echo "Docker Compose: ${docker_compose_version}" \  
&& echo \  
&& echo "Environment" \  
&& echo "===========" \  
&& env \  
&& echo \  
&& set -x \  
&& cd /tmp \  
&& ${CURL} -o docker.tgz \  
https://download.docker.com/linux/static/edge/x86_64/docker-${docker_version}.tgz
\  
&& tar -xf docker.tgz \  
&& chown root:root docker/docker \  
&& chmod 755 docker/docker \  
&& mv docker/docker /usr/bin \  
&& rm -rf docker* \  
&& groupadd -r docker \  
&& usermod -aG docker ${JENKINS_USER} \  
&& cd /usr/bin \  
&& ${CURL} -o docker-compose \  
https://github.com/docker/compose/releases/download/${docker_compose_version}/docker-
compose-Linux-x86_64 \  
&& chown root:root docker-compose \  
&& chmod 755 docker-compose  
  
USER ${JENKINS_USER}  
WORKDIR ${JENKINS_HOME}  

