FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get -y install python2.7-minimal gawk sed jq tar unzip git curl wget redir
socat traceroute haproxy rsync && \  
curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py && python2.7 get-
pip.py && rm get-pip.py && \  
pip \--no-cache-dir install awscli httpie yq  
  
ENV KUBECTL_VERSION 1.7.0  
RUN curl -o /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-
release/release/v$KUBECTL_VERSION/bin/linux/amd64/kubectl && \  
chmod +x /usr/local/bin/kubectl  
  

