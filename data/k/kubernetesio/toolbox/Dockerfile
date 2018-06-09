FROM buildpack-deps:latest  
  
RUN apt-get update && apt-get -y install unzip python-dev jq gettext  
  
WORKDIR /tmp  
  
ENV DOCKER_VERSION 18.03.1  
RUN curl -sSL
https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}-ce.tgz
-o docker.tgz \  
&& tar zxf docker.tgz -C /tmp \  
&& rm docker.tgz \  
&& mv /tmp/docker/* /usr/local/bin  
  
ENV COMPOSE_VERSION 1.21.2  
RUN curl -ssL
https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-
compose-Linux-x86_64 -o /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  
  
ENV K8S_VERSION 1.10.3  
RUN curl -sSL https://storage.googleapis.com/kubernetes-
release/release/v${K8S_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl  

