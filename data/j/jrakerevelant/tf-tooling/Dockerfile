# Tooling for terraform  
FROM chrisrock/openstack-cli  
MAINTAINER Jannis Rake-Revelant <jannis@rake-revelant.de>  
  
  
ENV TERRAFORM_VERSION 0.6.3  
  
  
RUN apt-get update -qq && \  
apt-get install -qy git wget make unzip && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/* && \  
wget -O /terraform.zip
http://dl.bintray.com/mitchellh/terraform/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip /terraform.zip -d usr/local/bin/ && \  
rm -f /terraform.zip

