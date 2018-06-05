FROM node:alpine  
LABEL maintainer="tpritsma@gmail.com"  
  
ENV PATH /google-cloud-sdk/bin:$PATH  
RUN apk --no-cache add \  
curl \  
python \  
py-crcmod \  
bash \  
libc6-compat \  
openssh-client \  
git \  
&& export CLOUD_SDK_VERSION="$(curl
https://cloud.google.com/sdk/downloads\#linux | \  
grep -Eoi '<a [^>]+>' | \  
grep -Eo 'href=[\"](.*)-linux-x86_64.tar.gz[\"]' | \  
sed 's/.*-\([0-9\\.][0-9\\.]*\).*/\1/')" \  
&& curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
ln -s /lib /lib64 && \  
gcloud config set core/disable_usage_reporting true && \  
gcloud config set component_manager/disable_update_check true && \  
gcloud config set metrics/environment github_docker_image  
VOLUME ["/root/.config"]

