FROM ubuntu:xenial  
  
RUN apt-get update -y && apt-get -y install \  
awscli \  
command-not-found \  
curl \  
dialog \  
dnsutils \  
ebtables \  
iproute2 \  
iptables \  
iputils-ping \  
jq \  
less \  
man-db \  
manpages \  
manpages-dev \  
ncurses-term \  
net-tools \  
netcat-openbsd \  
tcpdump \  
vim \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl \  
&& chmod +x ./kubectl \  
&& mv kubectl /usr/local/bin/ \  
&& curl -LO https://storage.googleapis.com/kubernetes-helm/helm-v2.8.0-linux-
amd64.tar.gz \  
&& tar zxf helm-v2.8.0-linux-amd64.tar.gz linux-amd64/helm \  
&& mv linux-amd64/helm /usr/local/bin/helm  
  

