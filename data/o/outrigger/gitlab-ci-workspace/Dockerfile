# docker build --build-arg DOCKER_ENGINE_VERSION=18.04 --tag outrigger/gitlab-
ci-workspace .  
# Default to the most recent v18 release at the time of the build.  
# To grab the most recent version, specify 'latest'  
ARG DOCKER_ENGINE_VERSION=18  
  
FROM docker:$DOCKER_ENGINE_VERSION  
  
# @see http://label-schema.org/rc1/  
LABEL maintainer="Phase2 <outrigger@phase2technology.com>" \  
# Replacement for the old MAINTAINER directive has fragmented.  
org.label-schema.vendor="Phase2 <outrigger@phase2technology.com>" \  
name="Outrigger GitLab CI Workspace" \  
org.label-schema.name="Outrigger GitLab CI Workspace" \  
org.label-schema.description="A GitLab CI workbench ready to support a
container-based pipeline." \  
org.label-schema.vcs-url="https://github.com/phase2/docker-gitlab-ci-
workspace" \  
org.label-schema.schema-version="1.0"  
  
RUN apk add --no-cache \  
bash \  
curl \  
openssl \  
py2-pip \  
&& \  
# Install Python tools  
pip install docker-compose \  
&& \  
# Install Kubernetes & Environment Management tools  
curl -o /usr/local/bin/kubectl -LO https://storage.googleapis.com/kubernetes-
release/release/$(curl -s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && \  
chmod +x /usr/local/bin/kubectl && \  
# Consider skipping the curlbash:
https://github.com/lachie83/k8s-helm/blob/v2.8.2/Dockerfile  
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get |
bash && \  
helm init --client-only  
  
COPY root /  

