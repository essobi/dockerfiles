FROM alpine:3.2  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
ENV VAULT_VERSION 0.2.0  
ENV VAULT_ADDR http://127.0.0.1:8200  
RUN apk --update add ca-certificates unzip && rm -rf /var/cache/apk/*  
  
ADD https://dl.bintray.com/mitchellh/vault/vault_0.2.0_linux_amd64.zip
/tmp/vault.zip  
RUN unzip /tmp/vault.zip -d /usr/local/bin  
RUN rm -f /tmp/vault.zip  
  
EXPOSE 8200  
ENTRYPOINT ["/usr/local/bin/vault"]  

