FROM alpine  
  
ENV VAULT_VERSION 0.4.1  
RUN apk add --update curl \  
&& curl -sSL -o "/tmp/vault.zip"
"https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip"
\  
&& cd /usr/local/bin \  
&& unzip -o "/tmp/vault.zip" \  
&& chmod +x vault && rm "/tmp/vault.zip" \  
&& apk del curl \  
&& rm /var/cache/apk/* -fR  
  
COPY entrypoint.sh /entrypoint.sh  
COPY vault.conf /etc/vault.conf  
  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 8200/tcp  

