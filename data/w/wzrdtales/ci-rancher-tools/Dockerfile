  
FROM wzrdtales/ci-base:latest  
  
MAINTAINER Tobias Gurtzick <magic@wizardtales.com>  
  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.12.5  
ENV DOCKER_SHA256
0058867ac46a1eba283e2441b1bb5455df846144f9d9ba079e97655399d4a2c6  
ENV RANCHER_VERSION 0.12.5  
ENV RANCHER_CLI 0.6.0  
USER root  
  
RUN curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& wget https://releases.rancher.com/cli/v${RANCHER_CLI}/rancher-linux-
amd64-v${RANCHER_CLI}.tar.gz -O- | tar -xzv ./rancher-v${RANCHER_CLI}/rancher
-O > /usr/bin/rancher \  
&& wget https://releases.rancher.com/compose/v${RANCHER_VERSION}/rancher-
compose-linux-amd64-v${RANCHER_VERSION}.tar.gz -O- | tar -xzv ./rancher-
compose-v${RANCHER_VERSION}/rancher-compose -O > /usr/bin/rancher-compose \  
&& chmod +x /usr/bin/rancher && chmod +x /usr/bin/rancher-compose \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER cirunner  

