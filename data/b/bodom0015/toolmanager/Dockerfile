#!/bin/bash  
#  
# Usage: docker build -t toolmanager .  
#  
FROM ubuntu:xenial  
  
# Install nginx / Node.js / npm  
RUN apt-get -qq update && \  
apt-get -qq install \  
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
apt-get -qq autoremove && \  
apt-get -qq autoclean && \  
apt-get -qq clean all && \  
rm -rf /var/cache/apk/* /tmp/*  
  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.10.3  
ENV DIND_COMMIT 3b5fac462d21ca164b3778647420016315289034  
  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& tar -xzvf docker.tgz \  
&& rm docker.tgz \  
&& docker -v \  
&& wget
"https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind" -O
/usr/local/bin/dind \  
&& chmod +x /usr/local/bin/dind \  
&& pip install flask-restful arrow jinja2 requests  
  
ENV TOOLSERVER_PORT 8083  
EXPOSE 8082  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["resolver"]  
  
# Install npm / bower dependencies + ToolManager UI  
COPY js/package.json js/bower.json /usr/share/nginx/html/  
RUN cd /usr/share/nginx/html/ && \  
npm install -g bower && \  
npm install && \  
bower install --config.interactive=false \--allow-root && \  
rm -rf /tmp/*  
  
COPY js /usr/share/nginx/html/  
  
COPY api /usr/local/bin/  
COPY data /usr/local/data/  

