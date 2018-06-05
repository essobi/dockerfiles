FROM docker:18.05  
ENV HELM_VERSION=v2.9.1  
ENV KOPS_VERSION=1.9.0  
ENV KUBECTL_VERSION=v1.10.3  
ENV KUBECONFIG=/srv/kubeconfig  
  
RUN apk add --no-cache git openssh-client bash tree jq ca-certificates curl  
  
RUN apk -Uuv add groff less python py-pip \  
&& pip install awscli \  
&& apk --purge -v del py-pip \  
&& rm /var/cache/apk/*  
  
RUN curl -LO https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \  
&& chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl  
  
RUN curl -LO https://storage.googleapis.com/kubernetes-
helm/helm-${HELM_VERSION}-linux-amd64.tar.gz \  
&& tar xvf helm-${HELM_VERSION}-linux-amd64.tar.gz \  
&& mv linux-amd64/helm /usr/local/bin/helm \  
&& helm init --client-only \  
&& helm repo add incubator http://storage.googleapis.com/kubernetes-charts-
incubator \  
&& rm -rf helm-${HELM_VERSION}-linux-amd64.tar.gz  
  
RUN curl -LO
https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-
linux-amd64 \  
&& chmod +x kops-linux-amd64 \  
&& mv kops-linux-amd64 /usr/local/bin/kops  
  
RUN wget $(curl -s https://api.github.com/repos/mikefarah/yq/releases/latest |
grep browser_download_url | grep linux_amd64 | cut -d '"' -f 4) \  
&& chmod 755 yq_linux_amd64 \  
&& mv yq_linux_amd64 /usr/local/bin/yq  
  
RUN touch ${KUBECONFIG}  
  
WORKDIR /srv  

