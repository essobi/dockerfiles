# We need etcdctl so this is a good base  
FROM quay.io/coreos/etcd:v3.2  
# Install cacerts, openssl, bash & jq  
RUN apk add --no-cache --update \  
bash \  
ca-certificates \  
openssl \  
&& wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 -O /usr/local/bin/dumb-init \  
&& wget https://dl.minio.io/client/mc/release/linux-amd64/mc -O
/usr/local/bin/mc \  
&& chmod +x \  
/usr/local/bin/mc \  
/usr/local/bin/dumb-init \  
&& apk del --no-cache --update \  
ca-certificates \  
openssl \  
&& rm -rf /var/cache/apk/*  
  
COPY src /  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
CMD [ "/backup.sh" ]

