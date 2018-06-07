FROM alpine:latest  
  
LABEL vendor="JobTeaser" \  
com.jobteaser.version="1.0.0" \  
com.jobteaser.release-date="2018-05-16" \  
maintainer="dev@jobteaser.com"  
  
ENV KUBECTL_VERSION="v1.10.1"  
ENV HELM_VERSION="v2.9.0"  
RUN apk add --no-cache \  
bash \  
jq \  
curl \  
git \  
make  
  
COPY wait_pod_readiness /usr/local/bin/  
  
RUN curl -L https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl \  
&& curl -L https://storage.googleapis.com/kubernetes-
helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -o /tmp/helm.tar.gz \  
&& tar -zxvf /tmp/helm.tar.gz -C /tmp \  
&& mv /tmp/linux-amd64/helm /usr/local/bin/helm \  
&& chmod +x /usr/local/bin/* \  
&& rm -rf /tmp/*  
  
CMD ["bash"]  

