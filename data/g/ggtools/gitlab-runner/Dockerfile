FROM gitlab/gitlab-runner:alpine-v10.0.2  
LABEL maintainer "christophe@labouisse.org"  
  
ENV DOCKER_PRIVILEGED=true \  
RUNNER_EXECUTOR=docker \  
DOCKER_IMAGE=docker:git \  
DOCKER_VOLUMES=/var/run/docker.sock:/var/run/docker.sock  
  
COPY patch/entrypoint.patch /  
  
# Patch the entrypoint rather than replace it to be more flexible  
RUN patch entrypoint entrypoint.patch  

