FROM docker:latest  
  
MAINTAINER bogdan.cismariu@imemento.com  
  
RUN apk update \  
&& apk add \--no-cache curl jq python py-pip \  
&& pip install awscli \  
&& curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s
https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name |
cut -d '"' -f 4)/kops-linux-amd64 \  
&& chmod +x kops-linux-amd64 \  
&& mv kops-linux-amd64 /usr/local/bin/kops \  
&& curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl \  
&& chmod +x kubectl \  
&& mv kubectl /usr/local/bin/kubectl  
  

