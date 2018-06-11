FROM centos:latest  
MAINTAINER youyo  
  
ENV VAGRANT_VERSION 1.8.1  
ENV PACKER_VERSION 0.10.1  
RUN yum install -y
https://releases.hashicorp.com/vagrant/${VAGRANT_VERSION}/vagrant_${VAGRANT_VERSION}_x86_64.rpm
unzip && \  
curl -O
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
&& \  
unzip packer_${PACKER_VERSION}_linux_amd64.zip && \  
mv packer /usr/local/bin/ && \  
rm -f packer_${PACKER_VERSION}_linux_amd64.zip && \  
vagrant plugin install vagrant-aws && \  
vagrant box add dummy https://github.com/mitchellh/vagrant-
aws/raw/master/dummy.box  

