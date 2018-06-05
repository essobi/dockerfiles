FROM phusion/baseimage:0.9.18  
ENV VAULT_VERSION=0.5.3 \  
DEBIAN_FRONTEND=noninteractive  
  
EXPOSE 8200  
RUN apt-get update && \  
apt-get upgrade -yq && \  
apt-get install -yq wget zip && \  
cd /tmp && \  
wget
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
&& \  
wget
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_SHA256SUMS
&& \  
wget
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_SHA256SUMS.sig
&& \  
grep vault_${VAULT_VERSION}_linux_amd64.zip vault_${VAULT_VERSION}_SHA256SUMS
| sha256sum -c && \  
unzip vault_${VAULT_VERSION}_linux_amd64.zip && \  
mv vault /usr/sbin/ && \  
mkdir -p /etc/service/vault && \  
apt-get -yq autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD vault.config /etc/  
  
ADD run.sh /etc/service/vault/run  
  
RUN chmod 0755 /etc/service/vault/run  

