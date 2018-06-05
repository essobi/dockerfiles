FROM debian:latest  
  
ENV KUBECTL_VERSION 1.9.0  
ENV HELM_VERSION 2.8.0  
ENV HELM_FILENAME helm-v${HELM_VERSION}-linux-amd64.tar.gz  
  
RUN apt-get update && apt install -y git openssh-client gnupg curl make vim
bash  
  
RUN set -ex \  
&& curl -LO https://storage.googleapis.com/kubernetes-
release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl \  
&& chmod +x ./kubectl \  
&& mv ./kubectl /usr/local/bin/kubectl  
  
RUN set -ex \  
&& curl -sSL https://storage.googleapis.com/kubernetes-helm/${HELM_FILENAME} |
tar xz \  
&& mv linux-amd64/helm /usr/local/bin/helm \  
&& rm -rf linux-amd64  
  
RUN helm init --client-only  
  
CMD ["/bin/bash"]

