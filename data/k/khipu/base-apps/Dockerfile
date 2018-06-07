FROM ubuntu:trusty  
MAINTAINER developers@khipu.com  
  
ARG CONFD_VERSION=0.11.0  
ARG ETCD_VERSION=2.2.5  
ARG GOSU_VERSION=1.7  
ARG KHIPU_GID=2000  
ARG KHIPU_UID=2000  
ARG ETCD_UID=2002  
ARG ETCD_GID=2002  
RUN echo 'America/Santiago' > /etc/timezone && \  
dpkg-reconfigure --frontend noninteractive tzdata && \  
dpkg-reconfigure --frontend noninteractive locales && \  
locale-gen en_US.UTF-8 && \  
update-locale LANG=en_US.UTF-8  
  
ENV LC_ALL en_US.UTF-8  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install curl s3cmd unzip wget -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN groupadd -r -g ${KHIPU_GID} khipu \  
&& useradd -r -u ${KHIPU_UID} -g ${KHIPU_GID} -s /sbin/nologin khipu \  
&& groupadd -r -g ${ETCD_GID} etcd \  
&& useradd -r -u ${ETCD_UID} -g ${ETCD_GID} -s /sbin/nologin etcd \  
&& gpasswd -a khipu etcd \  
&& mkdir -p /opt/khipu \  
&& cd /opt/khipu \  
&& mkdir bin etc share log var \  
&& chown -R khipu:khipu /opt/khipu  
  
RUN curl -o /usr/local/bin/confd -sSL
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd \  
&& curl -o etcd-v${ETCD_VERSION}-linux-amd64.tar.gz -sSL
https://github.com/coreos/etcd/releases/download/v${ETCD_VERSION}/etcd-v${ETCD_VERSION}-linux-
amd64.tar.gz \  
&& tar xzf etcd-v${ETCD_VERSION}-linux-amd64.tar.gz \  
&& mv etcd-v${ETCD_VERSION}-linux-amd64/etcdctl /usr/local/bin \  
&& rm -Rf etcd-v${ETCD_VERSION}-linux-amd64/ etcd-v${ETCD_VERSION}-linux-
amd64.tar.gz \  
&& curl -o /usr/local/bin/gosu -fsSL
https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64 \  
&& chmod +x /usr/local/bin/gosu  

