#  
# Bitbucket Pipeline - Python  
#  
# Use Alpine Base Image  
FROM alpine:3.7  
# Setup Container Deps  
RUN apk add --no-cache build-base git openssh openssh-client curl py-crcmod
bash libc6-compat docker  
  
#  
# Python Helper  
#  
RUN apk add --no-cache python3 python3-dev && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
rm -r /root/.cache && \  
pip3 install rancher-gitlab-deploy==1.5  
  
#  
# GCloud Helper  
#  
# Env Vars  
ENV CLOUD_SDK_VERSION=184.0.0  
ENV PATH /opt/google-cloud-sdk/bin:$PATH  
  
# Install Gcloud && Link Libraries  
RUN mkdir opt/ && cd /opt/ && curl -LO
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
ln -s /lib /lib64 && \  
gcloud config set core/disable_usage_reporting true && \  
gcloud config set component_manager/disable_update_check true  
  
# Kubectl  
RUN gcloud -q components install kubectl docker-credential-gcr  
  
#  
# Rancher Pipeline  
#  
# Install Rancher  
RUN cd /opt/ && curl -LO
https://github.com/rancher/cli/releases/download/v0.6.7/rancher-linux-
amd64-v0.6.7.tar.gz && \  
tar xzf rancher-linux-amd64-v0.6.7.tar.gz && \  
cd rancher-v0.6.7/ && mv rancher /usr/bin && cd .. && \  
rm -rf rancher-v0.6.7 rancher-linux-amd64-v0.6.7.tar.gz  
  
#  
# Entrypoint Pipeline  
#  
CMD ["/bin/sh"]

