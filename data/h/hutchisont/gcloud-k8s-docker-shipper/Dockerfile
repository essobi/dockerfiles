FROM ubuntu:16.04  
  
ENV KUBE_LATEST_VERSION="v1.8.5"  
ENV CLOUD_SDK_REPO="cloud-sdk-xenial"  
  
WORKDIR /usr/src/  
RUN apt-get update \  
&& apt-get install -y curl apt-transport-https ca-certificates \  
&& echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee
-a /etc/apt/sources.list.d/google-cloud-sdk.list \  
&& curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add \-
\  
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add \- \  
&& echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial
stable" | tee -a /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y curl git openssl wget gettext google-cloud-sdk docker-ce
\  
&& curl -L https://storage.googleapis.com/kubernetes-
release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl  

