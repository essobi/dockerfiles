FROM ubuntu:16.10  
# Install dependencies  
RUN apt-get update && apt-get install -y curl  
  
# Install Docker client  
RUN set -x \  
&& DOCKER_VERSION="17.03.0-ce" \  
&& curl -L -o /tmp/docker-$DOCKER_VERSION.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz \  
&& tar -xz -C /tmp -f /tmp/docker-$DOCKER_VERSION.tgz \  
&& mv /tmp/docker/* /usr/bin  
  
# Install Docker Compose  
RUN set -x \  
&& DOCKER_COMPOSE_VERSION="1.12.0" \  
&& curl -L -o /usr/local/bin/docker-compose
https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-
compose-`uname -s`-`uname -m` \  
&& chmod +x /usr/local/bin/docker-compose  
  
# Install Rancher CLI  
RUN set -x \  
&& RANCHER_CLI_VERSION="0.6.1" \  
&& curl -L -o /tmp/rancher-$RANCHER_CLI_VERSION.tgz
https://releases.rancher.com/cli/v$RANCHER_CLI_VERSION/rancher-linux-
amd64-v$RANCHER_CLI_VERSION.tar.gz \  
&& tar -xz -C /tmp -f /tmp/rancher-$RANCHER_CLI_VERSION.tgz \  
&& mv /tmp/rancher-v$RANCHER_CLI_VERSION/rancher /usr/bin  
  
# Install Rancher Compose  
RUN set -x \  
&& RANCHER_COMPOSE_VERSION="0.12.5" \  
&& curl -L -o /tmp/rancher-$RANCHER_COMPOSE_VERSION.tgz
https://releases.rancher.com/compose/v$RANCHER_COMPOSE_VERSION/rancher-
compose-linux-amd64-v$RANCHER_COMPOSE_VERSION.tar.gz \  
&& tar -xz -C /tmp -f /tmp/rancher-$RANCHER_COMPOSE_VERSION.tgz \  
&& mv /tmp/rancher-compose-v$RANCHER_COMPOSE_VERSION/rancher-compose /usr/bin  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD docker --version && docker-compose --version && rancher --version &&
rancher-compose --version  

