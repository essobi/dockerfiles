FROM golang:alpine  
  
ENV TERRAFORM_VERSION 0.11.1  
ENV CLOUD_SDK_VERSION 183.0.0  
# Google cloud SDK  
WORKDIR /  
ENV PATH /google-cloud-sdk/bin:$PATH  
RUN apk --no-cache add \  
curl \  
python \  
py-crcmod \  
bash \  
libc6-compat \  
openssh-client \  
openssh \  
git \  
&& curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
ln -s /lib /lib64  
  
RUN gcloud config set core/disable_usage_reporting true && \  
gcloud config set component_manager/disable_update_check true && \  
gcloud config set metrics/environment github_docker_image  
VOLUME ["/root/.config"]  
  
# Terraform  
ENV TF_DEV=true  
ENV TF_RELEASE=true  
  
WORKDIR $GOPATH/src/github.com/hashicorp/terraform  
RUN git clone https://github.com/hashicorp/terraform.git ./ && \  
git checkout v${TERRAFORM_VERSION} && \  
/bin/bash scripts/build.sh  
  

