FROM
alpine:3.7@sha256:8c03bb07a531c53ad7d0f6e7041b64d81f99c6e493cb39abba56d956b40eacbc  
  
RUN mkdir -p /tmp/workspace \  
&& mkdir -p /tmp/logs  
  
RUN apk --no-cache add git curl make bash openssh sudo jq  
  
COPY \--from=docker:17.12 /usr/local/bin/docker /bin/docker  
  
# Gcloud https://github.com/GoogleCloudPlatform/cloud-sdk-
docker/blob/master/alpine/Dockerfile  
ENV CLOUD_SDK_VERSION 201.0.0  
ENV PATH /google-cloud-sdk/bin:$PATH  
RUN apk --no-cache add \  
python \  
py-crcmod \  
libc6-compat \  
openssh-client  
RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
ln -s /lib /lib64 && \  
gcloud config set core/disable_usage_reporting true && \  
gcloud config set component_manager/disable_update_check true && \  
gcloud config set metrics/environment github_docker_image && \  
gcloud --version  
  
# Docker-compose  
RUN apk add --no-cache python2  
RUN apk add --no-cache --virtual build-deps py-pip  
RUN pip install --trusted-host pypi.python.org docker-compose  
  
RUN curl https://raw.githubusercontent.com/kadwanev/retry/master/retry -o
/usr/local/bin/retry \  
&& chmod +x /usr/local/bin/retry  

