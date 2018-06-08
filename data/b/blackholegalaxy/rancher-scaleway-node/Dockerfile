FROM blackholegalaxy/node-golang:latest  
  
MAINTAINER blackholegalaxy  
  
ENV RANCHER_CLI_VERSION=0.6.4  
ENV DOCKER_MACHINE_VERSION=0.12.2  
  
RUN apk add --no-cache --update --virtual .build-deps \  
binutils-gold \  
git \  
curl \  
g++ \  
gcc \  
gnupg \  
libgcc \  
linux-headers \  
make \  
python \  
openssl \  
&& curl -L
https://github.com/docker/machine/releases/download/v${DOCKER_MACHINE_VERSION}/docker-
machine-`uname -s`-`uname -m` > /usr/local/bin/docker-machine \  
&& chmod +x /usr/local/bin/docker-machine \  
&& go get -u github.com/scaleway/docker-machine-driver-scaleway \  
&& curl -L
"https://releases.rancher.com/cli/v${RANCHER_CLI_VERSION}/binaries/linux-
amd64/rancher.xz" | xzcat - > /usr/local/bin/rancher \  
&& chmod +x /usr/local/bin/rancher \  
&& apk del .build-deps \  
&& apk --no-cache add openssl ca-certificates \  
&& update-ca-certificates  

