FROM ubuntu:13.10  
MAINTAINER Tatsuru Watanabe <w.tatsuru@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install -y curl git unzip  
  
# ChefDK  
RUN curl -Ls -o /tmp/chefdk_0.1.0-1_amd64.deb https://opscode-omnibus-
packages.s3.amazonaws.com/ubuntu/13.10/x86_64/chefdk_0.1.0-1_amd64.deb \  
&& dpkg -i /tmp/chefdk_0.1.0-1_amd64.deb \  
&& rm -v /tmp/chefdk_0.1.0-1_amd64.deb  
  
# packer  
RUN curl -Ls -o /tmp/packer-0.6.0_linux_amd64.zip
https://dl.bintray.com/mitchellh/packer/0.6.0_linux_amd64.zip \  
&& mkdir -p /opt/packer/bin \  
&& unzip -d /opt/packer/bin /tmp/packer-0.6.0_linux_amd64.zip \  
&& rm -v /tmp/packer-0.6.0_linux_amd64.zip  
ENV PATH /opt/packer/bin:$PATH  

