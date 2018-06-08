FROM node:6.11  
LABEL maintainer "Lucid Programmer<lucidprogrammer@hotmail.com>"  
  
ENV terraform_version 0.10.8  
RUN apt-get update && apt-get install -y python-pip libpython-dev jq zip unzip
&& \  
pip install awscli && \  
curl -o terraform.zip
"https://releases.hashicorp.com/terraform/${terraform_version}/terraform_${terraform_version}_linux_amd64.zip"
&& \  
unzip terraform.zip -d /usr/local/bin/ && \  
rm terraform.zip  

