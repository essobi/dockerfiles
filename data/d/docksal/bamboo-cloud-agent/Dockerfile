#FROM openjdk:8  
#FROM openjdk:8-alpine  
FROM anapsix/alpine-java:8  
MAINTAINER Leonid Makarov <leonid.makarov@ffwagency.com>  
  
RUN apk add --update --no-cache \  
bash \  
sudo \  
curl \  
git \  
&& rm -rf /var/cache/apk/*  
  
# Download and install tools  
ENV DOCKER_VERSION=1.12.1  
ENV DOCKER_COMPOSE_VERSION=1.8.1  
RUN \  
# docker cli  
curl -sSL "https://get.docker.com/builds/$(uname -s)/$(uname
-m)/docker-${DOCKER_VERSION}.tgz" | tar zxf - && \  
mv docker/docker /usr/local/bin && rm -rf docker && \  
# docker-compose  
curl -sSL
"https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m`" -o /usr/local/bin/docker-compose && \  
# fin  
curl -sSL "https://raw.githubusercontent.com/docksal/docksal/develop/bin/fin"
-o /usr/local/bin/fin && \  
chmod +x /usr/local/bin/*  
  
RUN \  
mkdir -p /opt/bamboo && \  
# Create a non-root user with uid 1000 and access to sudo  
adduser -S -s /bin/bash -u 1000 -G users -D bamboo -h /opt/bamboo && \  
echo 'bamboo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# add startup script and capabilities file  
COPY bamboo-agent.sh /opt/bamboo/bamboo-agent.sh  
COPY bamboo-capabilities.properties /opt/bamboo/agent/bin/bamboo-
capabilities.properties  
  
# Misc configuration  
RUN \  
# Hardcore "bash-enabler"  
ln -sf /bin/bash /bin/sh && \  
# Fix /opt/bamboo folder permissions  
chown -R bamboo:users /opt/bamboo  
  
# All further RUN commands will run as the "bamboo" user  
USER bamboo  
ENV HOME /opt/bamboo  
  
# start Bamboo Cloud Agent  
CMD ["/opt/bamboo/bamboo-agent.sh"]  

