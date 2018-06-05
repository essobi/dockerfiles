FROM alpine:3.3  
RUN acme_tiny_revision="7a5a2558c8d6e5ab2a59b9fec9633d9e63127971" && \  
apk add --update python3 bash openssl ca-certificates git && \  
ln -s /usr/bin/python3 /usr/local/bin/python && \  
tempdir=$(mktemp -d) && \  
cd $tempdir && \  
git clone https://github.com/diafygi/acme-tiny.git && \  
cd $tempdir/acme-tiny && \  
git checkout $acme_tiny_revision && \  
cp acme_tiny.py /usr/local/bin/acme_tiny.py && \  
chmod +x /usr/local/bin/acme_tiny.py && \  
cd / && \  
rm -r $tempdir && \  
wget -O /usr/local/share/lets-encrypt-x3-cross-signed.pem
https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem && \  
apk del git && \  
rm -rf /var/cache/apk/* && \  
adduser -u 500 -H -D letsencrypt && \  
mkdir /acme-dir /data && \  
chown letsencrypt:letsencrypt /acme-dir /data  
  
ADD crt-manage /usr/local/bin/crt-manage  
  
VOLUME ["/acme-dir", "/data"]  
USER letsencrypt  
ENTRYPOINT ["/usr/local/bin/crt-manage"]  

