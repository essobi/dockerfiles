FROM ubuntu:16.04  
MAINTAINER pastakhov@yandex.ru  
  
# Install requered packages  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
git \  
nodejs \  
npm \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/apt/archives/*  
  
# Update npm  
RUN set -x; \  
npm install -g npm \  
&& ln -s /usr/bin/nodejs /usr/bin/node  
  
ENV RB_HOME=/var/lib/restbase \  
RB_DATA=/data \  
RB_USER=restbase \  
RB_VERSION=0.16.9  
# restbase setup  
RUN set -x; \  
# Core  
mkdir -p $RB_HOME \  
&& git clone \  
\--branch v${RB_VERSION} \  
\--single-branch \  
\--depth 1 \  
\--quiet \  
https://github.com/wikimedia/restbase.git \  
$RB_HOME \  
&& cd $RB_HOME \  
&& npm install \  
&& useradd -U -r -s /bin/bash $RB_USER \  
&& mkdir -p $RB_DATA \  
&& chown -R $RB_USER:$RB_USER $RB_DATA  
  
COPY run-restbase.sh /run-restbase.sh  
RUN chmod -v +x /run-restbase.sh  
  
COPY projects_docker.yaml $RB_HOME/projects/docker.yaml  
  
EXPOSE 7231  
CMD ["/run-restbase.sh"]  
VOLUME $RB_DATA  

