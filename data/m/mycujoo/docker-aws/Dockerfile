FROM cgswong/aws:latest  
  
ENV KUBERNETES_VERSION=1.7.2  
ENV TERRAFORM_VERSION=0.10.0  
ENV VAULT_VERSION=0.8.0  
# Install general dependencies  
RUN echo -e "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add --update-cache --allow-untrusted jq docker tar \  
consul-template@testing cfssl@testing make \  
curl ca-certificates bash  
  
# Download kubectl  
ADD https://storage.googleapis.com/kubernetes-
release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl
/usr/local/bin/kubectl  
  
# Download terraform  
ADD
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
/tmp/terraform.zip  
  
# Download vault  
ADD
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
/tmp/vault.zip  
  
ENV HOME=/config  
  
RUN set -x && \  
unzip /tmp/terraform -d /usr/local/bin && \  
unzip /tmp/vault -d /usr/local/bin && \  
chmod +x /usr/local/bin/kubectl && \  
chmod +x /usr/local/bin/terraform && \  
chmod +x /usr/local/bin/vault && \  
\  
# Create non-root user (with a randomly chosen UID/GUI).  
adduser kubectl -Du 2342 -h /config && \  
\  
# Basic check it works.  
kubectl version --client  
  
USER kubectl  

