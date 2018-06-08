FROM alpine:latest  
RUN apk add --no-cache openssl  
# https://docs.docker.com/engine/installation/linux/docker-
ce/binaries/#install-static-binaries  
RUN wget -q -O -
https://download.docker.com/linux/static/stable/x86_64/docker-17.12.0-ce.tgz |
tar -x -f - -z --strip-components=1 -v docker/docker  
# https://docs.docker.com/compose/install/  
RUN wget -q -O docker-compose
https://github.com/docker/compose/releases/download/1.19.0/docker-compose-
Linux-x86_64 && chmod +x docker-compose  
# https://www.terraform.io/intro/getting-started/install.html  
RUN wget -q -O terraform_0.11.7_linux_amd64.zip
https://releases.hashicorp.com/terraform/0.11.7/terraform_0.11.7_linux_amd64.zip
\  
&& unzip -o terraform_0.11.7_linux_amd64.zip terraform  
# https://docs.helm.sh/using_helm/#from-the-binary-releases  
RUN wget -q -O - https://storage.googleapis.com/kubernetes-
helm/helm-v2.9.0-linux-amd64.tar.gz | tar -x -f - -z --strip-components=1 -v
linux-amd64/helm  
  
FROM google/cloud-sdk:183.0.0-slim  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
git \  
kubectl \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY \--from=0 docker /usr/local/bin/  
COPY \--from=0 docker-compose /usr/local/bin/  
COPY \--from=0 terraform /usr/local/bin/  
COPY \--from=0 helm /usr/local/bin/  

