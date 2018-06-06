FROM ubuntu:latest  
MAINTAINER Ray Kao <ray.kao@microsoft.com>  
  
WORKDIR /root  
RUN apt-get update -y \--fix-missing\  
&& apt-get install -y \--no-install-recommends \  
apt-utils \  
software-properties-common \  
git-core \  
build-essential \  
libssl-dev libffi-dev \  
python-dev \  
wget \  
curl \  
unzip \  
apt-transport-https \  
jq \  
nano \  
vim \  
&& apt-add-repository ppa:ansible/ansible -y \  
&& apt-get update -y \--fix-missing \  
&& apt-get install -y ansible \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/
wheezy main" | tee /etc/apt/sources.list.d/azure-cli.list  
RUN apt-key adv --keyserver packages.microsoft.com \--recv-keys 417A0893  
RUN apt-get update \  
&& apt-get install azure-cli \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee
/etc/apt/sources.list.d/microsoft.list  
RUN apt-get update -y \  
&& apt-get install -y powershell \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget
https://releases.hashicorp.com/terraform/0.9.11/terraform_0.9.11_linux_amd64.zip
\  
&& unzip $(ls | grep terraform) \  
&& rm *.zip \  
&& mv terraform /usr/bin/  
  
RUN wget
https://releases.hashicorp.com/packer/1.0.2/packer_1.0.2_linux_amd64.zip \  
&& unzip $(ls | grep packer) \  
&& rm *.zip \  
&& mv packer /usr/bin/  
  
RUN useradd --create-home --shell /bin/bash kenobi  
USER kenobi  
WORKDIR /home/kenobi  

