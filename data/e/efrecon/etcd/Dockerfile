FROM gliderlabs/alpine:3.1  
MAINTAINER Emmanuel Frecon <emmanuel@sics.se>  
  
# Note that etcd catches all variables that start with ETCD_ and possibly  
# understands them as command-line arguments. So we use a variable that does  
# NOT start directly with ETCD to contain the version.  
ENV __ETCD_VERSION 2.0.9  
# The following enables fetching of the latest version of etcd solely based on  
# the version numbered declared above. This is why we require alpine and not  
# busybox, as we need curl to fetch the latest binaries (wget, which is
included  
# in busybox, does not support https links!)  
RUN apk --update add curl && \  
curl -sSL
https://github.com/coreos/etcd/releases/download/v$__ETCD_VERSION/etcd-v$__ETCD_VERSION-
linux-amd64.tar.gz | tar -zx -C /tmp -f - && \  
mv /tmp/etcd-v$__ETCD_VERSION-linux-amd64/etcd /usr/bin/etcd && \  
rm -rf /tmp/etcd-v$__ETCD_VERSION-linux-amd64 && \  
mkdir /data  
  
EXPOSE 4001 2380 7001 2379  
VOLUME /data  
  
ENTRYPOINT ["/usr/bin/etcd", "-data-dir", "/data"]  

