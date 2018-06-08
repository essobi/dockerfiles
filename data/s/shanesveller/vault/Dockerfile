FROM alpine:3.3  
ENV VAULT_VERSION=0.5.2 \  
VAULT_SHA256=7517b21d2c709e661914fbae1f6bf3622d9347b0fe9fc3334d78a01d1e1b4ec2  
RUN apk add --no-cache --update ca-certificates wget && \  
wget -O /vault_${VAULT_VERSION}_linux_amd64.zip
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
&& \  
echo "${VAULT_SHA256} vault_${VAULT_VERSION}_linux_amd64.zip" > /vault.sha256
&& \  
sha256sum -c /vault.sha256 && \  
cd /usr/local/bin && \  
unzip /vault_${VAULT_VERSION}_linux_amd64.zip && \  
apk del ca-certificates wget && \  
rm -rfv /vault* /var/cache/apk/*  
  
ENTRYPOINT ["/usr/local/bin/vault"]  

