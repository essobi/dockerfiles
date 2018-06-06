FROM ubuntu:16.04  
  
MAINTAINER ductamnguyen@anduintransact.com  
  
ENV VAULT_VERSION=0.8.3  
  
RUN apt-get -y update && \  
apt-get -y install wget curl python netcat jq unzip && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
wget
https://releases.hashicorp.com/vault/$VAULT_VERSION/vault_${VAULT_VERSION}_linux_amd64.zip
&& \  
unzip vault_${VAULT_VERSION}_linux_amd64.zip && \  
mv vault /usr/bin && \  
rm vault_${VAULT_VERSION}_linux_amd64.zip && \  
wget
https://raw.githubusercontent.com/anduintransaction/Dockerfiles/master/vault-
kube/vault-kube && \  
mv vault-kube /usr/bin && \  
chmod 755 /usr/bin/vault-kube  

