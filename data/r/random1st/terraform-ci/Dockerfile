FROM python:3.6  
MAINTAINER Roman Voronin version: 0.1  
RUN apt-get update && \  
apt-get install -y zip unzip jq && \  
wget
https://releases.hashicorp.com/terraform/0.11.3/terraform_0.11.3_linux_amd64.zip
&& \  
unzip terraform_0.11.3_linux_amd64.zip && \  
chmod +x terraform && \  
cp terraform /usr/local/bin/  
RUN wget
https://releases.hashicorp.com/packer/1.2.1/packer_1.2.1_linux_amd64.zip && \  
unzip packer_1.2.1_linux_amd64.zip && \  
chmod +x packer && \  
cp packer /usr/local/bin  
RUN pip install virtualenv awscli tox boto3 ansible  
RUN which terraform && terraform -v && \  
which packer && packer -v && \  
which aws && aws --version && \  
which tox && tox --version && \  
which ansible-playbook && ansible-playbook --version  
  

