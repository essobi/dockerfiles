# Docker file to run Hashicorp Vault (vaultproject.io)  
FROM alpine:3.2  
MAINTAINER Cihat Genc <cihat@catwithboots.com>  
  
ENV VAULT_VERSION 0.3.1  
ENV VAULT_TMP /tmp/vault.zip  
ENV VAULT_HOME /usr/local/bin  
ENV PATH $PATH:${VAULT_HOME}  
  
RUN apk --update add \  
wget \  
bash \  
ca-certificates &&\  
wget --quiet --output-document=${VAULT_TMP}
https://dl.bintray.com/mitchellh/vault/vault_${VAULT_VERSION}_linux_amd64.zip
&&\  
unzip ${VAULT_TMP} -d ${VAULT_HOME} &&\  
rm -f ${VAULT_TMP}  
  
ADD ./vault.json /etc/vault.json  
  
# Listener API tcp port and telemetry  
EXPOSE 8200 8125  
#CMD ["/usr/local/bin/vault", "server", "-config", "/etc/vault.json"]  
ENTRYPOINT ["/usr/local/bin/vault"]  
CMD [ "server", "-config=/etc/vault.json"]  

