FROM golang:1.9-alpine  
MAINTAINER zterry <zterry@qq.com>  
  
RUN apk add --no-cache git supervisor  
ENV ETCD_VERSION "3.2.14"  
ENV CONFD_VERSION "0.14.0"  
##### install polipo #####  
## https://hub.docker.com/r/vimagick/polipo/~/dockerfile/  
RUN set -xe \  
&& apk add --no-cache build-base openssl tar \  
&& wget https://github.com/jech/polipo/archive/master.zip -O polipo.zip \  
&& unzip polipo.zip \  
&& cd polipo-master \  
&& make \  
&& install polipo /usr/local/bin/ \  
&& cd .. \  
&& rm -rf polipo.zip polipo-master \  
&& mkdir -p /usr/share/polipo/www /var/cache/polipo \  
&& apk del build-base openssl  
  
##### install etcd #####  
## https://github.com/colebrumley/docker-etcd/blob/master/Dockerfile  
RUN apk add --update ca-certificates openssl tar && \  
wget
https://github.com/coreos/etcd/releases/download/v$ETCD_VERSION/etcd-v$ETCD_VERSION-
linux-amd64.tar.gz && \  
tar xzvf etcd-v$ETCD_VERSION-linux-amd64.tar.gz && \  
mv etcd-v$ETCD_VERSION-linux-amd64/etcd* /bin/ && \  
rm -Rf etcd-v$ETCD_VERSION-linux-amd64* /var/cache/apk/*  
  
#### install confd ####  
## https://github.com/smebberson/docker-alpine/blob/master/alpine-
confd/Dockerfile  
RUN apk add --update ca-certificates openssl tar && \  
wget
https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-$CONFD_VERSION-
linux-amd64 -O /bin/confd && \  
chmod +x /bin/confd  
  
#### install shadowsocks-local ####  
RUN go get github.com/shadowsocks/shadowsocks-go/cmd/shadowsocks-local  
  
ADD polipo.conf /etc/polipo.conf  
ADD supervisord.conf /etc/supervisord.conf  
  
EXPOSE 1080  
EXPOSE 8123  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

