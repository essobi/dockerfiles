FROM mhart/alpine-node  
  
ENV ETCD_HOST=127.0.0.1  
ENV ETCD_PORT=2379  
ENV S3_BUCKET=staging_etcdump  
ENV S3_OBJECT=etcd.json  
  
RUN apk -Uuv add bash git jq groff less python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  
RUN npm install -g arkenio/etcdump  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
ADD etcd_config.json /etcd_config.json  
  
ENTRYPOINT ["/start.sh"]  

