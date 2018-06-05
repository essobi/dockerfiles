FROM debian:8  
MAINTAINER Adrien Missemer <adrien.missemer@sap.com>  
  
#  
# Docker & Docker Compose install  
#  
ENV DEBIAN_FRONTEND noninteractive  
ENV COMPOSE_VERSION 1.8.0  
ENV MACHINE_VERSION 0.8.2  
RUN apt-get update -q && apt-get install -yq --no-install-recommends unzip
groff python2.7 curl apt-transport-https ca-certificates \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo deb https://apt.dockerproject.org/repo debian-jessie main >
/etc/apt/sources.list.d/docker.list \  
&& apt-get update \  
&& apt-get install -y docker-engine \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -o /usr/local/bin/docker-compose -L
"https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m`" \  
&& chmod +x /usr/local/bin/docker-compose \  
&& docker-compose version  
  
RUN curl -L
https://github.com/docker/machine/releases/download/v${MACHINE_VERSION}/docker-
machine-`uname -s`-`uname -m` >/usr/local/bin/docker-machine \  
&& chmod +x /usr/local/bin/docker-machine \  
&& docker-machine version  
  
# AWS CLI install (requires python, unzip and groff previously installed)  
RUN ln -s /usr/bin/python2.7 /usr/bin/python \  
&& curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" \  
&& unzip awscli-bundle.zip \  
&& ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
  
RUN useradd -ms /bin/bash dockerbash  
WORKDIR /home/dockerbash  
USER dockerbash  

