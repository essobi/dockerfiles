FROM alpine:latest  
  
ENV VAULT_VERSION 0.6.0  
RUN apk update && \  
apk add wget unzip  
  
RUN wget -nv
"https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip"
\--no-check-certificate && \  
unzip vault_${VAULT_VERSION}_linux_amd64.zip && \  
mv vault /usr/local/bin && \  
rm -f vault_${VAULT_VERSION}_linux_amd64.zip  
  
RUN apk del wget unzip  
  
EXPOSE 8200  

