FROM alpine  
  
ENV GCLOUD_VERSION=203  
ENV HELM_VERSION=2.9.1  
ENV KUBECTL_VERSION=1.9.7  
ENV ISTIO_VERSION=0.8.0  
ENV TERRAFORM_VERSION=11.3  
ENV SIGIL_VERSION=0.4.0  
LABEL maintainer="monstermesh-dev@objectcomputing.com"  
  
ENV PATH=/usr/local/google-cloud-sdk/bin:/usr/local/bin:$PATH  
  
WORKDIR /installer/cluster/gke  
  
RUN apk add --no-cache --update \  
bash \  
ca-certificates \  
curl \  
libc6-compat \  
make \  
python  
  
#kubectl  
ADD https://storage.googleapis.com/kubernetes-
release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl
/usr/local/bin/kubectl  
RUN chmod +x /usr/local/bin/kubectl  
  
#gcloud  
ADD https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-${GCLOUD_VERSION}.0.0-linux-x86_64.tar.gz /tmp  
RUN tar zxvf /tmp/google-cloud-sdk-${GCLOUD_VERSION}.0.0-linux-x86_64.tar.gz
-C /usr/local && \  
rm -f /tmp/google-cloud-sdk-${GCLOUD_VERSION}.0.0-linux-x86_64.tar.gz && \  
ln -s /lib /lib64 && \  
gcloud config set core/disable_usage_reporting true && \  
gcloud config set component_manager/disable_update_check true && \  
gcloud config set metrics/environment github_docker_image  
  
#helm  
ADD https://kubernetes-
helm.storage.googleapis.com/helm-v${HELM_VERSION}-linux-amd64.tar.gz /tmp  
RUN tar zxvf /tmp/helm-v${HELM_VERSION}-linux-amd64.tar.gz -C /usr/local
linux-amd64/helm && \  
mv /usr/local/linux-amd64/helm /usr/local/bin/helm && \  
rm -f /tmp/helm-v${HELM_VERSION}-linux-amd64.tar.gz  
  
#terraform  
ADD
https://releases.hashicorp.com/terraform/0.${TERRAFORM_VERSION}/terraform_0.${TERRAFORM_VERSION}_linux_amd64.zip
/tmp/  
RUN unzip /tmp/terraform_0.${TERRAFORM_VERSION}_linux_amd64.zip -d
/usr/local/bin/ && \  
rm -f /tmp/terraform_0.${TERRAFORM_VERSION}_linux_amd64.zip  
  
#istio  
ADD
https://github.com/istio/istio/releases/download/${ISTIO_VERSION}/istio-${ISTIO_VERSION}-linux.tar.gz
/tmp  
RUN tar xvf /tmp/istio-${ISTIO_VERSION}-linux.tar.gz -C /usr/local && \  
ln -s /usr/local/istio-${ISTIO_VERSION}/bin/istioctl /usr/local/bin/istioctl
&& \  
rm -f /tmp/istio-${ISTIO_VERSION}-linux.tar.gz  
  
#sigil  
ADD
https://github.com/gliderlabs/sigil/releases/download/v${SIGIL_VERSION}/sigil_${SIGIL_VERSION}_Linux_x86_64.tgz
/tmp  
RUN tar xvf /tmp/sigil_${SIGIL_VERSION}_Linux_x86_64.tgz -C /usr/local/bin &&
\  
rm -f /tmp/sigil_${SIGIL_VERSION}_Linux_x86_64.tgz  
  
# installer  
COPY README.md /installer/  
COPY cluster/gke/_templates/ /installer/cluster/gke/_templates/  
COPY cluster/modules/ /installer/cluster/modules/  
COPY k8s/ /installer/k8s/  
COPY cluster/gke/Makefile /installer/cluster/gke/  
COPY cluster/gke/create_cluster.sh /installer/cluster/gke/  
COPY cluster/gke/create_jenkins.sh /installer/cluster/gke/  

