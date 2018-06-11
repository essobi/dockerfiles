# PUBLIC IMAGE  
FROM ubuntu:16.04  
MAINTAINER Thomas Rampelberg <thomasr@vapor.io>  
  
ENV
OC_URL=https://github.com/openshift/origin/releases/download/v3.7.2/openshift-
origin-client-tools-v3.7.2-282e43f-linux-64bit.tar.gz  
  
RUN apt-get update \  
&& apt-get install -y \  
linux-image-extra-virtual \  
&& apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common \  
build-essential \  
python-pip \  
git \  
openssh-server \  
openssh-client \  
tar \  
gzip \  
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \  
&& add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable" \  
&& curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
\  
&& add-apt-repository \  
"deb https://packages.cloud.google.com/apt \  
cloud-sdk-$(lsb_release -cs) \  
main" \  
&& apt-get update \  
&& apt-get install -y \  
docker-ce \  
google-cloud-sdk \  
kubectl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install --upgrade pip && pip install --upgrade docker-compose  
  
RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get
| bash  
RUN curl -L ${OC_URL} | tar zx && cp openshift*/oc /usr/local/bin  

