FROM docker:1.13.1  
  
ENV KUBECTL_VERSION=v1.7.4  
ENV CLOUD_SDK_VERSION 198.0.0  
  
ENV PATH /google-cloud-sdk/bin:$PATH  
  
RUN apk add --no-cache \  
bash \  
curl \  
ca-certificates \  
git \  
python \  
py-crcmod \  
py-pip \  
gettext \  
ncurses \  
libc6-compat \  
openssh-client \  
jq \  
&& \  
echo "\nInstall awscli..." && \  
pip install awscli && \  
echo "\nInstall kubectl..." && \  
mkdir -p /usr/local/bin && \  
curl -L https://storage.googleapis.com/kubernetes-
release/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl \  
-o /usr/local/bin/kubectl && \  
chmod +x /usr/local/bin/kubectl && \  
echo "\nInstall gcloud..." && \  
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
mkdir -p /google-cloud-sdk && \  
tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
ln -s /lib /lib64 && \  
gcloud config set core/disable_usage_reporting true && \  
gcloud config set component_manager/disable_update_check true && \  
gcloud config set metrics/environment github_docker_image && \  
gcloud --version  
  
COPY bin/* /usr/local/bin/  

