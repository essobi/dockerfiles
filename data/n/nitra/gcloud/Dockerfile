FROM alpine  
  
#install deps and install gcloud  
RUN apk add \--update \--no-cache \  
bash \  
curl \  
python \  
&& curl https://sdk.cloud.google.com | bash -s -- \--disable-prompts  
  
ENV PATH="/root/google-cloud-sdk/bin:${PATH}"  
RUN gcloud config set disable_usage_reporting true \  
&& gcloud config set \--installation component_manager/disable_update_check
true \  
  
# Docker update  
&& wget
https://download.docker.com/linux/static/stable/x86_64/docker-18.03.0-ce.tgz
\--output-document="/tmp/docker.tgz" \  
&& tar -xz -C /tmp -f /tmp/docker.tgz \  
&& mv /tmp/docker/docker* /usr/local/bin/

