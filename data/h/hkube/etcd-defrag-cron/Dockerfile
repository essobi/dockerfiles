FROM alpine  
MAINTAINER yehiyam livneh  
ENV ETCD_VERSION 3.3.1  
ENV ETCD_ENDPOINT 127.0.0.1:4001  
ENV ETCDCTL_API=3  
RUN apk add --update ca-certificates \  
&& apk add --update -t deps curl \  
&& curl -L https://storage.googleapis.com/kubernetes-release/release/$(curl -s
https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl
\  
&& chmod +x /usr/local/bin/kubectl \  
&& curl -LOks
https://github.com/coreos/etcd/releases/download/v${ETCD_VERSION}/etcd-v${ETCD_VERSION}-linux-
amd64.tar.gz \  
&& tar zxvf etcd-v${ETCD_VERSION}-linux-amd64.tar.gz \  
&& cp etcd-v${ETCD_VERSION}-linux-amd64/etcdctl /usr/local/bin/ \  
&& rm -rf etcd-v* \  
&& chmod +x /usr/local/bin/etcdctl \  
&& apk del --purge deps \  
&& rm /var/cache/apk/*  
  
ADD run.sh /run.sh  
ENTRYPOINT [ "/run.sh" ]

