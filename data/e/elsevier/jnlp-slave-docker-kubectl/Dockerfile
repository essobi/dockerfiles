FROM jenkinsci/jnlp-slave:2.62  
MAINTAINER John Wards  
ENV DOCKER_VERSION=17.04.0-ce KUBECTL_VERSION=v1.8.9
DOCKER_COMPOSE_VERSION=1.17.0  
USER root  
  
# Install kubectl  
RUN curl -LO https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \  
&& chmod +x ./kubectl \  
&& mv ./kubectl /usr/local/bin/kubectl  
  
RUN apt-get update -qq && apt-get install -y -qq --no-install-recommends \  
make \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget -qO- https://get.docker.com/ | sh  
RUN curl -L "https://github.com/docker/compose/releases/download/1.8.1/docker-
compose-$(uname -s)-$(uname -m)" > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
RUN \  
curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py --user && \  
~/.local/bin/pip install awscli  

