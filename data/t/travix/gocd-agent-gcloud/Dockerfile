FROM travix/gocd-agent:18.5.0-alpine  
  
MAINTAINER Travix  
  
# install gcloud and some other tools  
ENV GCLOUD_VERSION=202.0.0 \  
HELM_VERSION=2.9.1 \  
ISTIO_VERSION=0.7.1 \  
CLOUDSDK_PYTHON_SITEPACKAGES="1"  
  
RUN apk --update-cache upgrade \  
&& apk add --update-cache \  
py-openssl \  
jq \  
libxml2-utils \  
xmlstarlet \  
xz \  
python \  
py-setuptools \  
gettext \  
perl \  
&& rm /var/cache/apk/* \  
&& curl -fSL
"https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-${GCLOUD_VERSION}-linux-x86_64.tar.gz" -o google-cloud-sdk-linux.tar.gz \  
&& tar -xf google-cloud-sdk-linux.tar.gz -C /var/go \  
&& rm -rf google-cloud-sdk-linux.tar.gz \  
&& /var/go/google-cloud-sdk/install.sh \  
&& /var/go/google-cloud-sdk/bin/gcloud config set disable_usage_reporting true
\  
&& /var/go/google-cloud-sdk/bin/gcloud components install alpha -q \  
&& /var/go/google-cloud-sdk/bin/gcloud components install beta -q \  
&& /var/go/google-cloud-sdk/bin/gcloud components install kubectl -q \  
&& /var/go/google-cloud-sdk/bin/gcloud config set --installation
component_manager/disable_update_check true \  
&& curl -fSL https://storage.googleapis.com/kubernetes-
helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz -o helm-v${HELM_VERSION}-linux-
amd64.tar.gz \  
&& tar -zxvf helm-v${HELM_VERSION}-linux-amd64.tar.gz \  
&& mv linux-amd64/helm /usr/local/bin/helm \  
&& rm -rf linux-amd64 \  
&& mkdir -p /opt/lego \  
&& curl -L
"https://github.com/istio/istio/releases/download/${ISTIO_VERSION}/istio-${ISTIO_VERSION}-linux.tar.gz"
| tar xz -C /var/go  
  
ENV PATH /opt/lego:/var/go/google-cloud-
sdk/bin:/var/go/istio-${ISTIO_VERSION}/bin:$PATH  
  
# copy the lego binary into the image  
COPY lego /opt/lego  
  
RUN chmod 777 /opt/lego/lego  

