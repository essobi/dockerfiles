FROM docker:stable  
  
ENV PACKER_VER=1.1.3  
ENV CLOUD_SDK_VERSION 185.0.0  
ENV PATH /google-cloud-sdk/bin:$PATH  
  
RUN apk update && apk upgrade && \  
apk add --no-cache \  
make \  
gcc \  
g++ \  
python \  
py-crcmod \  
bash \  
libc6-compat \  
openssh-client \  
openssl \  
git \  
curl \  
tar \  
jq \  
ca-certificates \  
sed \  
gettext  
  
# Packer  
RUN wget -O /tmp/packer.zip \  
"https://releases.hashicorp.com/packer/${PACKER_VER}/packer_${PACKER_VER}_linux_amd64.zip"
\  
&& unzip -o /tmp/packer.zip -d /usr/local/bin \  
&& rm -f /tmp/packer.zip  
  
# google cloud sdk  
RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
ln -s /lib /lib64 && \  
gcloud config set core/disable_usage_reporting true && \  
gcloud config set component_manager/disable_update_check true && \  
gcloud config set metrics/environment github_docker_image && \  
gcloud components install kubectl  
  
VOLUME ["/root/.config"]  

