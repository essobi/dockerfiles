FROM python:2.7-slim-stretch  
  
ADD kiya /usr/local/bin/kiya  
RUN chmod 755 /usr/local/bin/kiya  
  
WORKDIR /usr/local  
ADD https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-198.0.0-linux-x86_64.tar.gz gcloud.tar.gz  
RUN tar -xzpf gcloud.tar.gz && rm gcloud.tar.gz && ./google-cloud-
sdk/install.sh  
RUN echo source /usr/local/google-cloud-sdk/path.bash.inc >> ~/.bashrc  
RUN mkdir -p /root/.config/gcloud  
  
RUN apt-get update && apt-get install -y \  
curl \  
gnupg \  
apt-transport-https  
  
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key
add -  
RUN echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" >>
/etc/apt/sources.list.d/kubernetes.list  
RUN apt-get update && apt-get install -y kubectl && rm -rf
/var/lib/apt/lists/*  

