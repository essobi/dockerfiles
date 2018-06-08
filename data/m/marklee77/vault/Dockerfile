FROM alpine:latest  
MAINTAINER Mark Stillwell <mark@stillwell.me>  
  
RUN apk update && \  
apk add openssl && \  
rm /var/cache/apk/*  
  
RUN wget
https://releases.hashicorp.com/vault/0.3.1/vault_0.3.1_linux_amd64.zip -O
vault.zip && \  
unzip vault.zip && \  
mv vault /usr/local/bin &&\  
rm vault.zip  
  
WORKDIR /tmp  
  
ADD config.json ./config.json  
ADD startvault.sh ./startvault.sh  
RUN chmod 755 startvault.sh  
  
ENV VAULT_ADDR=http://127.0.0.1:8200  
EXPOSE 8200  
RUN mkdir /var/lib/vault  
VOLUME ["/var/lib/vault"]  
  
CMD ./startvault.sh  

