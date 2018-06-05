FROM alpine:3.4  
MAINTAINER Luca Corbo <lu.corbo@gmail.com>  
  
WORKDIR /app  
  
ENV BATS_VERSION "0.4.0"  
ENV KUBE_LATEST_VERSION="v1.4.6"  
RUN apk --no-cache add \  
bash \  
curl \  
zip \  
unzip \  
ansible  
  
RUN mkdir -p /tmp/bats && cd /tmp/bats \  
&& curl -sSL https://github.com/sstephenson/bats/archive/v$BATS_VERSION.tar.gz
-o bats.tgz \  
&& tar -zxf bats.tgz \  
&& cd bats-$BATS_VERSION \  
&& /bin/bash ./install.sh /usr/local \  
&& cd / \  
&& rm -rf /tmp/bats  
  
CMD ["/usr/local/bin/bats"]  
  
RUN apk add --update ca-certificates \  
&& apk add --update -t deps curl \  
&& curl -L https://storage.googleapis.com/kubernetes-
release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl \  
&& apk del --purge deps \  
&& rm /var/cache/apk/*  

