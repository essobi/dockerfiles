FROM node:latest  
  
RUN apt-get update && apt-get install -y jq  
  
# Install kubectl  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl \  
&& chmod +x ./kubectl \  
&& mv ./kubectl /usr/local/bin/kubectl \  
&& kubectl version --client  
  
# Install kops  
RUN curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s
https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name |
cut -d '"' -f 4)/kops-linux-amd64 \  
&& chmod +x kops-linux-amd64 \  
&& mv kops-linux-amd64 /usr/local/bin/kops \  
&& kops version  
  
# Install helm  
RUN curl -L https://kubernetes-helm.storage.googleapis.com/helm-$(curl -s
https://api.github.com/repos/kubernetes/helm/releases/latest | grep tag_name |
cut -d '"' -f 4)-linux-amd64.tar.gz -o helm.tar.gz \  
&& tar -zxvf helm.tar.gz \  
&& rm helm.tar.gz \  
&& chmod +x linux-amd64/helm \  
&& mv linux-amd64/helm /usr/local/bin/helm \  
&& rm -rf linux-amd64  
  
ENV AGENT_VERSION=0.1.1  
# RUN npm init  
RUN npm install aws-sdk  
RUN npm install promise  
RUN npm install bluebird  
  
COPY src /src  
RUN mkdir -p /data  
  
WORKDIR /src  
  
CMD ./agent.sh  

