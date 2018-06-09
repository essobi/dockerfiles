FROM alpine:3.3  
RUN apk add --update bash curl jq groff less python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm -rf /var/cache/apk/*  
  
ADD etcd-v2.3.0-linux-amd64/etcd /usr/bin/etcd  
ADD onstart.sh /root/onstart.sh  
  
EXPOSE 2379 2380  
ENTRYPOINT ["/root/onstart.sh"]  

