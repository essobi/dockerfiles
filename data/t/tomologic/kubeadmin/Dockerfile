FROM alpine:3.7  
RUN apk add --no-cache bash curl make python  
  
# Prepare installation of the k8s tools  
ENV PATH=/opt/google-cloud-sdk/bin:$PATH \  
GOOGLE_CLOUD_SDK_VERSION=203.0.0 \  
CLOUDSDK_CORE_DISABLE_PROMPTS=1 \  
CLOUDSDK_PYTHON_SITEPACKAGES=1 \  
GCLOUD_SDK_URL=https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-
sdk.tar.gz  
  
RUN mkdir /opt  
RUN curl -sL $GCLOUD_SDK_URL | tar -C /opt -xzf -  
# Install Google Cloud SDK and ensure version is the one specified  
RUN /opt/google-cloud-sdk/install.sh \  
\--usage-reporting=false \  
\--path-update=true \  
\--bash-completion=true \  
\--additional-components alpha beta \  
&& (gcloud version | grep -q "Google Cloud SDK $GOOGLE_CLOUD_SDK_VERSION" \  
|| gcloud components update --version $GOOGLE_CLOUD_SDK_VERSION)  
RUN gcloud config set \--installation component_manager/disable_update_check
true  
  
# Install newer kubectl than the one bundled with gcloud SDK  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl \  
&& chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl  
  
# Helm  
ENV HELM_VERSION v2.9.1  
RUN mkdir /opt/helm \  
&& curl -sL https://kubernetes-
helm.storage.googleapis.com/helm-${HELM_VERSION}-linux-amd64.tar.gz \  
| tar -C /opt/helm -xzvf - \  
&& mv /opt/helm/linux-amd64/helm /bin/helm \  
&& rm -rvf /opt/helm  
RUN helm init --client-only  
# Besides stable charts add incubator charts too  
RUN helm repo add incubator https://kubernetes-charts-
incubator.storage.googleapis.com/  
  
COPY ./initialize.sh /opt/google-cloud-sdk/bin/initialize  
  
CMD ["/bin/bash"]  

