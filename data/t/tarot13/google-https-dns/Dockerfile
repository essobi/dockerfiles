FROM alpine  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN apk add --update --no-cache curl wget ca-certificates libcap && \  
update-ca-certificates && \  
mkdir -p /usr/bin && \  
cd /usr/bin && \  
wget -qO- https://github.com/techotaku/google-https-
dns/releases/download/v20180108/google-https-dns_linux-amd64-20180108.tar.gz |
tar xz && \  
mv google-https-dns_* google-https-dns && \  
setcap CAP_NET_BIND_SERVICE=+eip /usr/bin/google-https-dns && \  
apk del libcap && \  
rm -rf /var/cache/apk/* && \  
chmod +x /entrypoint.sh  
  
USER nobody  
  
ENTRYPOINT ["/entrypoint.sh"]

