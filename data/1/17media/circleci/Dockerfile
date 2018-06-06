FROM alpine:3.6  
  
ENV CLOUD_SDK_VERSION 170.0.1  
ENV PATH /google-cloud-sdk/bin:$PATH  
  
RUN apk --no-cache add --virtual .run-deps \  
build-base \  
git \  
openssh-client \  
parallel \  
curl \  
ca-certificates \  
tar \  
gzip \  
coreutils \  
jq \  
docker && \  
apk --no-cache add -X http://dl-cdn.alpinelinux.org/alpine/v3.4/community
--virtual .run-deps \  
hub && \  
  
# Add gcloud  
apk --no-cache add --virtual .build-deps \  
curl && \  
curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz | tar xz && \  
ln -s /lib /lib64 && \  
apk --no-cache add --virtual .run-deps \  
curl \  
python \  
py-crcmod \  
bash \  
libc6-compat \  
openssh-client \  
git && \  
gcloud config set core/disable_usage_reporting true && \  
gcloud config set component_manager/disable_update_check true && \  
gcloud config set metrics/environment github_docker_image  

