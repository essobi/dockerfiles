FROM travix/gocd-agent-gcloud:18.5.0  
MAINTAINER Travix  
  
ENV PACKER_VERSION=1.1.3  
# install packages  
RUN curl -fSL
"https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip"
-o packer.zip \  
&& unzip packer.zip -d /opt/packer \  
&& rm -f packer.zip  
  
ENV PATH="/opt/packer:$PATH"

