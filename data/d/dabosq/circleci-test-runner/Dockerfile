########################################  
# Unofficial image to run my tests in CircleCI 2.0  
#  
# Installs:  
# - docker and docker-compose (to build and test)  
# - jq and awscli (for ecs-deploy script)  
# - latest version of node.js and a TAP-to-xUnit output  
# converter (to format test output for CircleCI)  
# - two scripts for ECS deployment, an older  
# shell script and newer Python script  
########################################  
  
FROM buildpack-deps:jessie  
  
########################################  
# install Pip package manager, and jq (command-line JSON editor)  
  
RUN apt-get update && apt-get install -y python-dev python-pip jq  
  
########################################  
# install official Amazon Web Services CLI  
  
RUN pip install awscli ecs-deploy  
  
########################################  
# install Node.js 8.11, based on steps in official image  
# https://github.com/nodejs/docker-node  
  
ENV NODE_VERSION 8.11.1  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
########################################  
# install TAP-to-xUnit output converter  
# https://github.com/aghassemi/tap-xunit  
  
RUN npm install -g tap-xunit  
  
########################################  
# install main docker CLI from official binaries  
  
ENV DOCKER_VERSION 17.03.0-ce  
  
RUN curl -L
"https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz" -o
"/tmp/docker-$DOCKER_VERSION.tgz" \  
&& tar -xz -C /tmp -f "/tmp/docker-$DOCKER_VERSION.tgz" && mv /tmp/docker/*
/usr/local/bin  
  
########################################  
# install docker-compose from official binaries  
  
RUN curl -L
"https://github.com/docker/compose/releases/download/1.11.2/docker-
compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  
  
########################################  
# install ecs-deploy shell script  
  
RUN curl -L https://raw.githubusercontent.com/silinternational/ecs-
deploy/develop/ecs-deploy -o /usr/local/bin/ecs-deploy \  
&& chmod +x /usr/local/bin/ecs-deploy  

