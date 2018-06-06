FROM alpine  
  
USER root  
  
RUN apk add --no-cache git curl ca-certificates bash jq python  
  
ARG kube_version=1.9.8  
ARG kops_version=1.9.0  
ARG helm_version=2.8.1  
# Install kubectl  
RUN curl -s -L https://storage.googleapis.com/kubernetes-
release/release/v${kube_version}/bin/linux/amd64/kubectl >
/usr/local/bin/kubectl && \  
chmod +x /usr/local/bin/kubectl  
  
# Install kops  
RUN curl -s -L
https://github.com/kubernetes/kops/releases/download/${kops_version}/kops-
linux-amd64 > /usr/local/bin/kops && \  
chmod +x /usr/local/bin/kops  
  
# Install helm  
RUN curl -s -L https://kubernetes-
helm.storage.googleapis.com/helm-v${helm_version}-linux-amd64.tar.gz | tar xzv
&& \  
chmod +x ./linux-amd64/helm && \  
mv ./linux-amd64/helm /usr/local/bin/helm && \  
mkdir -p $(helm home)/plugins  
  
# Install helm-template  
RUN helm plugin install https://github.com/technosophos/helm-template  
  
# Install aws-cli  
RUN curl -s -L https://bootstrap.pypa.io/get-pip.py > get-pip.py && \  
python get-pip.py && \  
pip install awscli  

