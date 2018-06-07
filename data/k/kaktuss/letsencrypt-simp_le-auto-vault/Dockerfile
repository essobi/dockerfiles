FROM alpine:3.6  
ENV VAULT_VERSION=0.9.0  
ENV
VAULT_SHA256=801ce0ceaab4d2e59dbb35ea5191cfe8e6f36bb91500e86bec2d154172de59a4  
  
RUN \  
apk add --no-cache --virtual .build-deps \  
curl \  
unzip \  
  
&& cd /usr/local/bin \  
&& curl -L
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
-o vault_${VAULT_VERSION}_linux_amd64.zip \  
&& echo -n "$VAULT_SHA256 vault_${VAULT_VERSION}_linux_amd64.zip" | sha256sum
-c - \  
&& unzip vault_${VAULT_VERSION}_linux_amd64.zip \  
&& rm vault_${VAULT_VERSION}_linux_amd64.zip \  
  
&& apk del .build-deps  
  
ENV CERTS_DIR=  
ENV VAULT_ADDR=  
ENV VAULT_TOKEN=  
  
ENV VAULT_PATH=secret/certificates  
  
COPY store /etc/periodic/15min/store  
COPY renew /etc/periodic/weekly/renew  
  
CMD ["crond", "-f"]  

