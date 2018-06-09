FROM debian:9  
MAINTAINER Tobias Munk <tobias@diemeisterei.de>  
  
# Install system packages  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
bash \  
curl \  
ca-certificates \  
expect \  
make \  
nano \  
openssh-client \  
python \  
sshpass \  
unzip \  
&& apt-get clean  
  
# Docker tools, installed to /opt/local  
# for older versions, use a schmunk42/toolbox:5.x.x image  
RUN mkdir -p /opt/local/bin  
  
# v7.0  
ENV MACHINE_VERSION_CURRENT=0.12.2 \  
DOCKER_VERSION_CURRENT=17.05.0-ce \  
COMPOSE_VERSION_CURRENT=1.16.1  
RUN curl -L
https://github.com/docker/machine/releases/download/v${MACHINE_VERSION_CURRENT}/docker-
machine-`uname -s`-`uname -m` >/opt/local/bin/docker-
machine-${MACHINE_VERSION_CURRENT} && \  
chmod +x /opt/local/bin/docker-machine-${MACHINE_VERSION_CURRENT}  
  
RUN curl -L
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION_CURRENT}.tgz
> /tmp/docker-${DOCKER_VERSION_CURRENT}.tgz && \  
cd /tmp && tar -xzf ./docker-${DOCKER_VERSION_CURRENT}.tgz && \  
rm /tmp/docker-${DOCKER_VERSION_CURRENT}.tgz && \  
mv /tmp/docker/docker /opt/local/bin/docker-${DOCKER_VERSION_CURRENT} && \  
chmod +x /opt/local/bin/docker-${DOCKER_VERSION_CURRENT}  
  
RUN curl -L
https://github.com/docker/compose/releases/download/${COMPOSE_VERSION_CURRENT}/docker-
compose-`uname -s`-`uname -m` > /opt/local/bin/docker-
compose-${COMPOSE_VERSION_CURRENT} && \  
chmod +x /opt/local/bin/docker-compose-${COMPOSE_VERSION_CURRENT}  
  
# Install Docker Cloud CLI  
RUN curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install docker-cloud  
  
RUN ln -s /opt/local/bin/docker-machine-${MACHINE_VERSION_CURRENT}
/opt/local/bin/docker-machine  
RUN ln -s /opt/local/bin/docker-${DOCKER_VERSION_CURRENT}
/opt/local/bin/docker  
RUN ln -s /opt/local/bin/docker-compose-${COMPOSE_VERSION_CURRENT}
/opt/local/bin/docker-compose  
  
ENV PATH=/opt/local/bin:$PATH  

