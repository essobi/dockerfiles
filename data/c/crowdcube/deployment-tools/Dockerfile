FROM alpine:3.6  
  
ENV KOPS_VERSION=1.7.1  
ENV KUBECTL_VERSION=v1.8.2  
ENV HELM_VERSION=v2.7.0  
ENV AWSCLI_VERSION=1.14.56  
ENV DOCKER_VERSION=17.05.0-r0  
ENV YARN_VERSION=0.23.3-r0  
  
RUN apk --no-cache update \  
&& apk --no-cache add ca-certificates curl python py-pip py-setuptools groff
less git openssh docker="${DOCKER_VERSION}" yarn="${YARN_VERSION}" bash jq \  
&& apk --no-cache add \--virtual build-dependencies curl \  
&& pip --no-cache-dir install awscli=="${AWSCLI_VERSION}" \  
&& curl -LO --silent --show-error
https://github.com/kubernetes/kops/releases/download/"${KOPS_VERSION}"/kops-
linux-amd64 \  
&& mv kops-linux-amd64 /usr/local/bin/kops \  
&& curl -LO https://storage.googleapis.com/kubernetes-
release/release/"${KUBECTL_VERSION}"/bin/linux/amd64/kubectl \  
&& mv kubectl /usr/local/bin/kubectl \  
&& curl -LO https://storage.googleapis.com/kubernetes-
helm/helm-"${HELM_VERSION}"-linux-amd64.tar.gz \  
&& tar -zxvf helm-"${HELM_VERSION}"-linux-amd64.tar.gz \  
&& mv linux-amd64/helm /usr/local/bin/helm \  
&& chmod +x /usr/local/bin/kops /usr/local/bin/kubectl /usr/local/bin/helm \  
&& apk del --purge build-dependencies \  
&& rm -rf helm-"${HELM_VERSION}"-linux-amd64.tar.gz  
  
CMD ["/bin/sh"]  

