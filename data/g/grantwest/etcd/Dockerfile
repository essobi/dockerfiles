FROM alpine:latest  
  
ARG etcd_tag=v3.2.5  
RUN apk add --update ca-certificates openssl tar && \  
wget
https://github.com/coreos/etcd/releases/download/$etcd_tag/etcd-$etcd_tag-
linux-amd64.tar.gz -O etcd.tar.gz && \  
tar xzvf etcd.tar.gz && \  
mv etcd-$etcd_tag-linux-amd64/etcd* /bin/ && \  
apk del --purge tar openssl && \  
rm -Rf etcd.tar.gz etcd-$etcd_tag-linux-amd64 /var/cache/apk/*  
  
VOLUME /data  
EXPOSE 2379 2380 4001 7001  
ADD run.sh /bin/run.sh  
#ENTRYPOINT ["/bin/run.sh"]  
CMD /bin/etcd  

