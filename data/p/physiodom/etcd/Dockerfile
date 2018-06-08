# etcd container : Service discovery  
FROM alpine:3.3  
ENV ETCD_VERSION="2.2.1"  
LABEL version=${ETCD_VERSION} \  
description="service discovery etcd v${ETCD_VERSION}" \  
buitdate="August, 2015"  
  
MAINTAINER Fabrice Le Coz <fabrice.lecoz@telecomsante.com>  
  
ADD
https://github.com/coreos/etcd/releases/download/v${ETCD_VERSION}/etcd-v${ETCD_VERSION}-linux-
amd64.tar.gz .  
  
RUN mkdir /opt && \  
tar xzvf etcd-v${ETCD_VERSION}-linux-amd64.tar.gz -C /opt && \  
ln -sfn /opt/etcd-v${ETCD_VERSION}-linux-amd64/etcd /bin && \  
ln -sfn /opt/etcd-v${ETCD_VERSION}-linux-amd64/etcdctl /bin && \  
rm etcd-v${ETCD_VERSION}-linux-amd64.tar.gz  
  
COPY start.sh .  
  
VOLUME ["/data"]  
  
EXPOSE 2379 4001  
CMD ["./start.sh"]  

