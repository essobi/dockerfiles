FROM alpine:3.6  
MAINTAINER developers@khipu.com  
  
ARG CONFD_VERSION=0.12.0-alpha3  
ARG ETCD_VERSION=3.2.1  
ARG GOSU_VERSION=1.10  
ARG KHIPU_GID=2000  
ARG KHIPU_UID=2000  
ARG ETCD_UID=2002  
ARG ETCD_GID=2002  
RUN apk add --update curl bash gettext su-exec \  
&& rm -rf /var/cache/apk/*  
  
RUN adduser -u ${ETCD_UID} -D -H etcd \  
&& adduser -u ${KHIPU_UID} -D -H khipu \  
&& adduser khipu etcd \  
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

