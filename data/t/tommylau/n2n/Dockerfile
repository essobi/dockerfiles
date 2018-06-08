FROM alpine:3.4  
  
MAINTAINER Tommy Lau <tommy@gen-new.com>  
  
RUN buildDeps=" \  
build-base \  
cmake \  
git \  
linux-headers \  
openssl-dev \  
"; \  
set -x \  
&& apk add --update openssl \  
&& apk add $buildDeps \  
&& mkdir -p /usr/src \  
&& cd /usr/src \  
&& git clone https://github.com/meyerd/n2n \  
&& cd n2n/n2n_v2 \  
&& cmake . \  
&& make install \  
&& cd / \  
&& rm -fr /usr/src/n2n \  
&& apk del $buildDeps \  
&& rm -rf /var/cache/apk/*  
  
CMD ["/usr/local/sbin/supernode", "-l", "53", "-f"]  

