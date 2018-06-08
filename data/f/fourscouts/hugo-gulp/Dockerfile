FROM ubuntu:latest  
RUN apt-get update -yq && apt-get install -yq curl python-setuptools software-
properties-common apt-transport-https lsb-release  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN curl -Lo hugo_0.41_Linux-64bit.deb
https://github.com/gohugoio/hugo/releases/download/v0.41/hugo_0.41_Linux-64bit.deb
&& dpkg -i hugo_0.41_Linux-64bit.deb  
RUN apt-get install -yq nodejs && npm install -g gulp@4.0.0 gulp-cli  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
edge"  
RUN apt-get update -yq && apt-get install -yq docker-ce  
  
RUN curl -O https://storage.googleapis.com/kubernetes-
release/release/v1.10.0/bin/linux/amd64/kubectl && \  
chmod +x kubectl && \  
mv kubectl /usr/bin  
  
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \  
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a
/etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add \- &&
\  
apt-get update -yq && \  
apt-get install -yq google-cloud-sdk  

