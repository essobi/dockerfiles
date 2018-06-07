FROM alpine:3.3  
RUN apk add --update bash curl jq groff less python py-pip && \  
pip install awscli && \  
pip install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-
bootstrap-latest.tar.gz && \  
rm -rf /var/cache/apk/*  
  
ADD etcd-v2.3.0-linux-amd64/etcd /usr/bin/etcd  
ADD etcd-v2.3.0-linux-amd64/etcdctl /usr/bin/etcdctl  
ADD onstart.sh /root/onstart.sh  
ADD start_monitor.sh /root/start_monitor.sh  
  
EXPOSE 2379 2380  
ENTRYPOINT ["/root/onstart.sh"]  

