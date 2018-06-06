FROM alpine:3.4  
  
ARG DUMB_INIT_VERSION=1.1.3  
ARG SECRETARY_VERSION=0.9.0  
  
COPY FWDRootCA.pem /tmp/FWDRootCA.crt  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN apk add --no-cache ca-certificates openssl tzdata bash curl && \  
wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 && \  
wget -O /usr/bin/secretary
https://github.com/meltwater/secretary/releases/download/${SECRETARY_VERSION}/secretary-
Linux-x86_64 && \  
chmod +x /usr/bin/secretary /usr/bin/dumb-init && \  
mv -f /tmp/FWDRootCA.crt /usr/local/share/ca-certificates/ && \  
/usr/sbin/update-ca-certificates && \  
mkdir /lib64 && \  
ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 && \  
apk del openssl && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/entrypoint.sh"]  

