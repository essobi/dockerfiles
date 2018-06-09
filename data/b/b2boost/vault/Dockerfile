FROM alpine:latest  
MAINTAINER Luis Muniz <luis.muniz@b2boost.com>  
ENV REFRESHED_AT 2016-09-30  
ENV VAULT_VERSION 0.6.1  
ENV AWS_S3_BUCKET <BUCKET NAME>  
ENV AWS_ACCESS_KEY_ID <CHANGEME>  
ENV AWS_SECRET_ACCESS_KEY <CHANGEME>  
ENV AWS_DEFAULT_REGION <CHANGEME>  
  
# x509 expects certs to be in this file only.  
RUN apk update && apk add openssl ca-certificates && rm -rf /var/cache/apk/*  
  
# Download, unzip the given version of vault and set permissions  
RUN wget -qO /tmp/vault.zip
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
&& \  
unzip -d /bin /tmp/vault.zip && rm /tmp/vault.zip && chmod 755 /bin/vault  
  
EXPOSE 8200  
VOLUME "/config"  
COPY config/s3.hcl /config/server.hcl  
  
ENTRYPOINT ["/bin/vault"]  
CMD server -config=/config/server.hcl  

