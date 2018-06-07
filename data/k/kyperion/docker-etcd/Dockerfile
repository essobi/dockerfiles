FROM kyperion/docker-alpine:latest  
  
ARG GIT_HASH  
  
LABEL version="3.0.3"  
LABEL app="etcd"  
LABEL REPO="https://github.com/Kyperion/docker-etcd"  
  
# see https://github.com/coreos/etcd/issues/4234  
ENV _ETCD_VERSION=3.0.3  
ADD start.sh /opt/etcd/bin/start.sh  
ADD kubernetes /opt/etcd/kubernetes  
  
RUN \  
chmod +x /opt/etcd/bin/start.sh \  
&& touch /opt/etcd/etcd.conf \  
&& chmod 0755 /opt/etcd/kubernetes/*.sh  
  
RUN apk add --no-cache --update \  
tar \  
&& wget -q -O -
"https://github.com/coreos/etcd/releases/download/v${_ETCD_VERSION}/etcd-v${_ETCD_VERSION}-linux-
amd64.tar.gz" \  
| tar xzv --strip-components 1 -C /opt/etcd/bin/ etcd-v${_ETCD_VERSION}-linux-
amd64/etcd etcd-v${_ETCD_VERSION}-linux-amd64/etcdctl \  
&& apk del --purge tar  
  
VOLUME /var/lib/etcd  
  
CMD ["/opt/etcd/bin/start.sh"]  
  
EXPOSE 2379 2380  
# if it got this far, label it witht he git hash  
LABEL GIT_HASH=$GIT_HASH  
ENV GIT_HASH=$GIT_HASH

