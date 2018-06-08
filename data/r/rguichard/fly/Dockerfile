FROM ubuntu:16.04  
MAINTAINER Romain Guichard <rgu@osones.io>  
ENV K8S_VERSION v1.10.0  
RUN apt update && apt install -yf ca-certificates jq  
  
ADD https://ci.rguichard.fr/api/v1/cli?arch=amd64&platform=linux /usr/bin/fly  
RUN chmod +x /usr/bin/fly  
ADD https://storage.googleapis.com/kubernetes-
release/release/"$K8S_VERSION"/bin/linux/amd64/kubectl /usr/bin/kubectl  
RUN chmod +x /usr/bin/kubectl  

