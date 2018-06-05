FROM buildpack-deps:jessie  
  
# install dev tools to be able to build npm modules  
# node-canvas: https://github.com/Automattic/node-canvas/wiki/Installation---
Ubuntu-and-other-Debian-based-systems  
RUN apt-get update && apt-get install -y \  
build-essential \  
jq \  
libcairo2-dev \  
libjpeg62-turbo-dev \  
libpango1.0-dev \  
libgif-dev \  
python \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
  
COPY n-master/bin/n /data/n/bin/  
COPY scripts /data/buildpack/  
  
  
RUN set -ex \  
&& groupadd -g 2567 app \  
&& useradd -rm -u 2567 -g app app \  
\  
&& mkdir -p /data/app /data/n/bin /data/cache \  
&& chmod u+x /data/n/bin/n \  
\  
&& chmod u+x /data/buildpack/*.sh \  
\  
&& sleep 2 \  
&& /data/buildpack/install-node.sh \  
\  
&& chown -R app:app /data \  
\  
&& ln -s /data/buildpack/run.sh /data/run.sh \  
&& ln -s /data/buildpack/install-modules.sh /data/install-modules.sh  
  

