FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND=noninteractive  
ENV CLOUD_SDK_REPO="cloud-sdk-xenial"  
RUN apt-get update && apt-get -y install git curl apt-transport-https python-
pip python-dev  
RUN echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" |
tee -a /etc/apt/sources.list.d/google-cloud-sdk.list  
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -  
RUN apt-get update && apt-get -y install google-cloud-sdk  
  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl  
RUN chmod +x ./kubectl  
RUN mv ./kubectl /usr/local/bin/kubectl  

