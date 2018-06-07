FROM khipu/base-alpine-s6:edge  
MAINTAINER developers@khipu.com  
  
ENV ETCD_VERSION=2.2.5  
ENV CONFD_VERSION=0.11.0  
ADD developers@khipu.com-55de074c.rsa.pub /etc/apk/keys/  
  
#RUN echo "http://s3.amazonaws.com/alpine.khipu.com/packages/main" >>
/etc/apk/repositories \  
RUN apk add --update curl tzdata \  
&& rm -rf /var/cache/apk/*  
  
RUN cp /usr/share/zoneinfo/America/Santiago /etc/localtime \  
&& echo "America/Santiago" > /etc/timezone  
  
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
amd64.tar.gz  

