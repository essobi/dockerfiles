# Inspired by
https://github.com/voxxit/dockerfiles/blob/master/vault/Dockerfile  
FROM jalaziz/base:alpine  
  
ENV VAULT_VERSION 0.5.2  
RUN wget -q
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
\  
&& unzip vault_${VAULT_VERSION}_linux_amd64.zip \  
&& mv vault /usr/local/bin/ \  
&& rm -f vault_${VAULT_VERSION}_linux_amd64.zip  
  
EXPOSE 8200  
VOLUME [ "/config" ]  
  
ENTRYPOINT [ "/usr/local/bin/vault" ]  
CMD [ "server", "-config=/config" ]  
  

