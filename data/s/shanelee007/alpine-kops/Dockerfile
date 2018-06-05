FROM alpine:latest  
  
ENV KOPS_VERSION=1.9.0  
# https://kubernetes.io/docs/tasks/kubectl/install/  
# latest stable kubectl: curl -s https://storage.googleapis.com/kubernetes-
release/release/stable.txt  
ENV KUBECTL_VERSION=v1.10.2  
ENV TERRAFORM_VERSION=0.11.7  
ENV HELM_VERSION=v2.8.2  
  
RUN apk --no-cache update \  
&& apk --no-cache add ca-certificates python py-pip py-setuptools groff less \  
&& apk --no-cache add --virtual build-dependencies curl \  
&& pip --no-cache-dir install awscli \  
&& curl -LO --silent --show-error
https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-
linux-amd64 \  
&& mv kops-linux-amd64 /usr/local/bin/kops \  
&& curl -LO https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \  
&& mv kubectl /usr/local/bin/kubectl \  
&& curl -LO
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
\  
&& unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \  
&& mv terraform /usr/local/bin/terraform \  
&& curl -LO https://storage.googleapis.com/kubernetes-
helm/helm-${HELM_VERSION}-linux-amd64.tar.gz \  
&& tar -zxvf helm-${HELM_VERSION}-linux-amd64.tar.gz \  
&& mv linux-amd64/helm /usr/local/bin/helm \  
&& chmod +x /usr/local/bin/kops /usr/local/bin/kubectl
/usr/local/bin/terraform /usr/local/bin/helm \  
&& apk del --purge build-dependencies \  
&& rm -rf terraform_${TERRAFORM_VERSION}_linux_amd64.zip \  
&& rm -rf helm-${HELM_VERSION}-linux-amd64.tar.gz  
  
CMD ["/bin/sh"]  

