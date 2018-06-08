FROM mhart/alpine-node:10  
RUN apk add --no-cache tar gzip libc6-compat curl wget git openssh-client bash
g++  
  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.12.6  
ENV DOCKER_SHA256
cadc6025c841e034506703a06cf54204e51d0cadfae4bae62628ac648d82efdd  
# ENV RANCHER_COMPOSE_VERSION v0.12.5  
ENV KOPS_VERSION 1.9.0  
ENV KUBECTL_VERSION v1.10.1  
RUN set -x \  
# && wget -O /tmp/rancher-compose-linux-
amd64-${RANCHER_COMPOSE_VERSION}.tar.gz "https://github.com/rancher/rancher-
compose/releases/download/${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-
amd64-${RANCHER_COMPOSE_VERSION}.tar.gz" \  
# && tar -xf /tmp/rancher-compose-linux-
amd64-${RANCHER_COMPOSE_VERSION}.tar.gz -C /tmp \  
# && mv /tmp/rancher-compose-${RANCHER_COMPOSE_VERSION}/rancher-compose
/usr/local/bin/rancher-compose \  
# && rm -R /tmp/rancher-compose-linux-amd64-${RANCHER_COMPOSE_VERSION}.tar.gz
/tmp/rancher-compose-${RANCHER_COMPOSE_VERSION}\  
# && chmod +x /usr/local/bin/rancher-compose \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v \  
&& curl -LO https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \  
&& mv kubectl /usr/local/bin/ \  
&& chmod +x /usr/local/bin/kubectl \  
&& curl -fSL
https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-
linux-amd64 -o kops \  
&& mv kops /usr/local/bin/ \  
&& chmod +x /usr/local/bin/kops  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["bash"]  

