FROM alpine:latest  
  
RUN \  
set -x && \  
apk update && \  
apk -Uuv add groff less python py2-pip bash jq mysql-client curl wget ca-
certificates openssl && \  
pip install awscli yq==2.2.0 && \  
apk --purge -v del py2-pip && \  
rm /var/cache/apk/*  
  
# Install kubectl  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl \  
&& chmod +x ./kubectl \  
&& mv ./kubectl /usr/local/bin/kubectl \  
&& kubectl version --client  
  
# Install kops  
RUN curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s
https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name |
cut -d '"' -f 4)/kops-linux-amd64 \  
&& chmod +x kops-linux-amd64 \  
&& mv kops-linux-amd64 /usr/local/bin/kops \  
&& kops version  
  
# Install helm  
RUN curl -L https://kubernetes-helm.storage.googleapis.com/helm-$(curl -s
https://api.github.com/repos/kubernetes/helm/releases/latest | grep tag_name |
cut -d '"' -f 4)-linux-amd64.tar.gz -o helm.tar.gz \  
&& tar -zxvf helm.tar.gz \  
&& rm helm.tar.gz \  
&& chmod +x linux-amd64/helm \  
&& mv linux-amd64/helm /usr/local/bin/helm \  
&& rm -rf linux-amd64  
  
RUN LATEST_VAULT_RELEASE=$(curl -s
https://api.github.com/repos/hashicorp/vault/tags | jq --raw-output
.[0].name[1:]) \  
&& curl -L
https://releases.hashicorp.com/vault/${LATEST_VAULT_RELEASE}/vault_${LATEST_VAULT_RELEASE}_linux_amd64.zip
-o vault.zip \  
&& unzip vault.zip \  
&& rm vault.zip \  
&& chmod +x vault \  
&& mv vault /usr/local/bin/vault  
  
  

