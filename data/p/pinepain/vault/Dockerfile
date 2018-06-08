FROM ubuntu:16.04  
ENV VAULT_VERSION=0.9.0  
RUN apt-get update && \  
apt-get install -y --no-install-recommends ca-certificates curl unzip && \  
curl -s -L
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
-o vault_${VAULT_VERSION}_linux_amd64.zip && \  
unzip vault_${VAULT_VERSION}_linux_amd64.zip -d /usr/local/bin/ && \  
mkdir /vault && \  
rm vault_${VAULT_VERSION}_linux_amd64.zip && \  
apt-get remove -y ca-certificates curl unzip && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /vault  
EXPOSE 8200 8201  
ENV VAULT_ADDR=http://127.0.0.1:8200  
ENV LOG_LEVEL=info  
  
COPY config.hcl config.hcl  
  
CMD vault server -log-level=$LOG_LEVEL -config=/vault/config.hcl  

