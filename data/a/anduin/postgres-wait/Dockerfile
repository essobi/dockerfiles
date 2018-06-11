FROM postgres:9.6  
MAINTAINER ductamnguyen@anduintransact.com  
  
ENV VAULT_VERSION=0.8.3  
RUN apt-get -y update && apt-get install -y jq wget unzip && \  
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
chmod 755 /usr/bin/vault-kube && \  
apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
ADD wait.sh /opt/wait.sh  
ADD run.sh /opt/run.sh  
  
CMD exec /opt/run.sh  

