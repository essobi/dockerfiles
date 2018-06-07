FROM ubuntu:16.04  
#BASE IMAGE INCLUDING :  
# Terraform, ansible, awscli  
RUN apt-get update -y && \  
apt-get install software-properties-common python-software-properties -y && \  
apt-add-repository ppa:ansible/ansible  
  
RUN apt-get update -y && \  
apt-get install jq curl unzip git ansible python-pip -y  
  
RUN pip install awscli  
  
RUN cd /tmp && curl -o terraform.zip
https://releases.hashicorp.com/terraform/0.9.4/terraform_0.9.4_linux_amd64.zip  
  
RUN cd /tmp && unzip terraform.zip  
RUN chmod +x /tmp/terraform && cp /tmp/terraform /usr/bin/terraform  

