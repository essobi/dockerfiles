FROM alpine:3.7  
  
ARG DUMB_INIT_VERSION=1.2.1  
ARG SECRETARY_VERSION=0.10.1  
  
COPY FWDRootCA.pem /tmp/FWDRootCA.crt  
  
RUN mkdir -p /opt/fwd && addgroup -S fwd && \  
adduser -u 999 -h /opt/fwd -s /bin/false -D -G fwd fwd && \  
apk add --no-cache ca-certificates openssl tzdata bash curl && \  
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
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

