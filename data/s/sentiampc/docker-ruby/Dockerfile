FROM ruby:2.1  
  
RUN apt-get update -qqy && apt-get install -qqy \  
awscli \  
build-essential \  
cmake \  
colordiff \  
unzip \  
wget \  
zip \  
&& rm -rf /var/lib/apt/lists  
  
RUN cd /tmp \  
; wget
https://releases.hashicorp.com/packer/1.0.0/packer_1.0.0_linux_amd64.zip \  
; wget http://stedolan.github.io/jq/download/linux64/jq \  
; unzip *.zip \  
; install -t /usr/bin -g root -o root -m 0755 /tmp/packer* /tmp/jq \  
; rm -f /tmp/*.zip /tmp/packer* /tmp/jq  

