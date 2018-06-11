FROM alpine:latest  
MAINTAINER RafPe <me@rafpe.ninja>  
  
ENV VAULT_VERSION 0.7.2  
RUN apk update && apk add openssl ca-certificates && rm -rf /var/cache/apk/*  
  
RUN wget -qO /tmp/vault.zip
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
\  
&& unzip -d /usr/bin/ /tmp/vault.zip \  
&& rm /tmp/vault.zip \  
&& chmod 755 /usr/bin/vault  
  
VOLUME /data  
  
EXPOSE 8200  
ENTRYPOINT ["/usr/bin/vault"]  
CMD ["server", "-dev-listen-address=0.0.0.0:8200", "-dev"]  

