FROM hashicorp/terraform:0.9.2  
  
RUN apk add --update --no-cache \  
build-base \  
jq \  
linux-headers \  
libffi-dev \  
openssl-dev \  
python \  
python-dev \  
py-pip \  
tree \  
&& cd /tmp \  
&& curl -o packer_0.12.3_linux_amd64.zip
https://releases.hashicorp.com/packer/0.12.3/packer_0.12.3_linux_amd64.zip \  
&& unzip packer_0.12.3_linux_amd64.zip \  
&& mv packer /bin/ \  
&& rm packer_0.12.3_linux_amd64.zip \  
&& pip install --upgrade pip \  
&& pip install ansible \  
awscli \  
&& mkdir /cloud-ops  
  
WORKDIR /cloud-ops  
  
# override terraform entrypoint  
ENTRYPOINT ["ash"]  

