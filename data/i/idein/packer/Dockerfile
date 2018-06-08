FROM ubuntu:18.04  
  
ENV PACKER_VERSION=1.2.3  
ENV
PACKER_SHA256SUM=822fe76c2dfe699f187ef8c44537d10453a1545db620e40b345cf6991a690f7d  
  
RUN apt-get update\  
&& apt-get install --no-install-recommends -y curl git unzip ca-certificates
openssh-client\  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sLO
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip\  
&& echo "$PACKER_SHA256SUM packer_${PACKER_VERSION}_linux_amd64.zip" |
sha256sum -c --strict -\  
&& unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /bin\  
&& rm -f packer_${PACKER_VERSION}_linux_amd64.zip  
  
RUN apt-get update\  
&& apt-get install --no-install-recommends -y software-properties-common\  
&& apt-add-repository ppa:ansible/ansible\  
&& apt-get update\  
&& apt-get install --no-install-recommends -y ansible\  
&& rm -rf /var/lib/apt/lists/*  
  
ENV USER root  

