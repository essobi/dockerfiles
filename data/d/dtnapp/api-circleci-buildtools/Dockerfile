FROM dtnapp/jdk-8-alpine-maven  
  
#Configure version variables  
ENV CLOUD_SDK_VERSION=172.0.0 \  
TERRAFORM_VERSION=0.10.8  
#Configure paths  
ENV PATH=/google-cloud-sdk/bin:$PATH  
  
#Install gcloud  
RUN apk --no-cache add \  
curl \  
python \  
py-crcmod \  
bash \  
libc6-compat \  
openssh-client \  
git \  
openssl \  
jq \  
gettext \  
&& rm -rf /var/cache/apk/* \  
&& curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
ln -s /lib /lib64 && \  
gcloud config set core/disable_usage_reporting true && \  
gcloud config set component_manager/disable_update_check true && \  
gcloud config set metrics/environment github_docker_image  
  
#Install Docker  
RUN apk add --update docker && rm -rf /var/cache/apk/*  
  
#Install Terraform  
RUN apk add --update unzip \  
&& curl -s -o terraform.zip
"https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip"
\  
&& unzip terraform.zip \  
&& mv ./terraform /usr/local/bin  
  
#Install Kubectl  
RUN gcloud components install kubectl  
  
#Install npm for supertest  
RUN apk add --update nodejs nodejs-npm  

