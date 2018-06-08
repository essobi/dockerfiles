# Use lastest Ubuntu LTS  
FROM ubuntu:16.04  
# Install base packages  
# Inspired by https://github.com/GoogleCloudPlatform/cloud-sdk-
docker/blob/master/debian/Dockerfile  
RUN apt-get update --quiet \  
&& apt-get install --quiet --yes \  
apt-transport-https \  
curl \  
gcc \  
git \  
lsb-release \  
python-dev \  
python-setuptools \  
python-pip \  
tzdata \  
wget  
  
# Configure GCloud  
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" \  
&& echo "deb https://packages.cloud.google.com/apt ${CLOUD_SDK_REPO} main" >
/etc/apt/sources.list.d/google-cloud-sdk.list \  
&& curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
\  
&& apt-get update  
  
# Install GCloud 181.0.0-0  
RUN apt-get install --quiet --yes google-cloud-sdk=181.0.0-0 \  
&& gcloud config set core/disable_usage_reporting true \  
&& gcloud config set component_manager/disable_update_check true \  
&& gcloud config set metrics/environment github_docker_image  
  
# Install GCloud Components 181.0.0-0  
RUN apt-get install --quiet --yes \  
google-cloud-sdk-app-engine-go=181.0.0-0 \  
google-cloud-sdk-app-engine-python=181.0.0-0 \  
google-cloud-sdk-datastore-emulator=181.0.0-0  
  
# Install AWS  
RUN pip install awscli  
  
# Download Bazel 0.9.0  
RUN wget https://storage.googleapis.com/bazel-
apt/pool/jdk1.8/b/bazel/bazel_0.9.0_amd64.deb  
  
# Install Bazel 0.9.0  
RUN apt-get install --quiet --yes ./bazel_0.9.0_amd64.deb  
  
# Remove Bazel deb  
RUN rm bazel_0.9.0_amd64.deb  

