#!/bin/bash  
#  
# Usage: docker build -t toolmanager .  
#  
FROM ubuntu:xenial  
  
# Managed Data Tools  
COPY data /usr/local/data/  
  
# ToolManager API  
COPY api /usr/local/bin/  
  
# Install nginx / Node.js / npm  
RUN apt-get -qq update && \  
apt-get -qq install \  
ca-certificates \  
openssl \  
# btrfs-progs \  
e2fsprogs \  
# e2fsprogs-extra \  
# xz \  
xfsprogs \  
curl \  
docker.io \  
git \  
iptables \  
nginx \  
npm \  
python \  
python-dev \  
python-pip \  
sudo \  
unzip \  
vim \  
wget && \  
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \  
apt-get -qq install nodejs && \  
ln -s /usr/local/bin/node /usr/local/bin/nodejs && \  
pip install flask-restful arrow jinja2 && \  
apt-get -qq autoremove && \  
apt-get -qq autoclean && \  
apt-get -qq clean all && \  
rm -rf /var/cache/apk/* /tmp/*  
  
# Install npm / bower dependencies + ToolMaanger UI  
COPY js /usr/share/nginx/html/  
RUN cd /usr/share/nginx/html/ && \  
npm install -g bower && \  
npm install && \  
bower install --config.interactive=false \--allow-root && \  
rm -rf /tmp/*  
  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.12.6  
ENV DOCKER_SHA256
cadc6025c841e034506703a06cf54204e51d0cadfae4bae62628ac648d82efdd  
  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v  
  
RUN set -x \  
&& sh -c 'addgroup --system dockremap' \  
&& sh -c 'adduser --system --ingroup dockremap dockremap' \  
&& sh -c 'echo dockremap:165536:65536 > /etc/subuid' \  
&& sh -c 'echo dockremap:165536:65536 > /etc/subgid'  
  
ENV DIND_COMMIT 3b5fac462d21ca164b3778647420016315289034  
  
RUN wget
"https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind" -O
/usr/local/bin/dind \  
&& chmod +x /usr/local/bin/dind  
  
COPY dockerd-entrypoint.sh /usr/local/bin/  
  
VOLUME /var/lib/docker  
ENV TOOLSERVER_PORT 8083  
EXPOSE 2375 8082  
ENTRYPOINT ["dockerd-entrypoint.sh"]  
CMD []  
  

