FROM ubuntu:16.04  
MAINTAINER "Rsrp Sinr" <rsrp.sinr@gmail.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
locales \  
&& rm -rf /var/lib/apt/lists/*  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
#---------------------------------------------  
# EtcdD  
#---------------------------------------------  
ENV ETCDD_VERSION 0.2  
ENV ETCD_VERSION 3.1.12  
RUN apt-get update && \  
apt-get install -y \  
ca-certificates \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget -O -
https://github.com/coreos/etcd/releases/download/v${ETCD_VERSION}/etcd-v${ETCD_VERSION}-linux-
amd64.tar.gz | tar xz -C /tmp && \  
mv /tmp/etcd-v${ETCD_VERSION}-linux-amd64/etcd /usr/bin/etcd && \  
mv /tmp/etcd-v${ETCD_VERSION}-linux-amd64/etcdctl /usr/bin/etcdctl && \  
rm -rf /tmp/etcd-v${ETCD_VERSION}-linux-amd64  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 700 /entrypoint.sh  
  
ADD app.sh /app.sh  
RUN chmod 700 /app.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

