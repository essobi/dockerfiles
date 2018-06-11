FROM alpine:latest  
  
MAINTAINER Tony Deng <wolf.deng@gmail.com>  
  
ENV ETCD_INSTALL_VERSION v2.3.7  
# install etcd  
RUN apk add --update ca-certificates openssl tar && \  
wget
https://github.com/coreos/etcd/releases/download/$ETCD_INSTALL_VERSION/etcd-$ETCD_INSTALL_VERSION-
linux-amd64.tar.gz && \  
tar zxvf etcd-$ETCD_INSTALL_VERSION-linux-amd64.tar.gz && \  
mv etcd-$ETCD_INSTALL_VERSION-linux-amd64/etcd* /bin/ && \  
apk del --purge tar openssl && \  
rm -Rf etcd-$ETCD_INSTALL_VERSION-linux-amd64* /var/cache/apk/*  
  
# listen on all interfaces  
ENV ECTD_LISTEN_CLIENT_URLS=http://0.0.0.0:2379,http://0.0.0.0:4001  
ENV ETCD_ADVERTISE_CLIENT_URLS=http://0.0.0.0:2379  
VOLUME /data  
EXPOSE 2379 2380 4001 7001  
ADD run.sh /bin/run.sh  
RUN chmod -R 755 /bin/run.sh  
ENTRYPOINT ["/bin/run.sh"]  

