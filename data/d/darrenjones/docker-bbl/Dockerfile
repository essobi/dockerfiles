FROM ubuntu:16.04  
MAINTAINER Darren Jones: 0.1  
RUN apt-get update  
RUN apt-get install -y wget curl git tree jq build-essential zlibc zlib1g-dev
ruby ruby-dev openssl libxslt-dev libxml2-dev libssl-dev libreadline6
libreadline6-dev libyaml-dev libsqlite3-dev sqlite3 unzip  
RUN curl -O https://s3.amazonaws.com/bosh-cli-artifacts/bosh-cli-2.0.48-linux-
amd64  
RUN chmod +x bosh-cli-*  
RUN mv bosh-cli-* /usr/local/bin/bosh  
  
RUN wget
https://releases.hashicorp.com/terraform/0.11.2/terraform_0.11.2_linux_amd64.zip  
RUN unzip terraform_0.11.2_linux_amd64.zip  
RUN chmod +x terraform  
RUN mv terraform /usr/bin/terraform  
RUN wget https://github.com/cloudfoundry/bosh-
bootloader/releases/download/v5.11.6/bbl-v5.11.6_linux_x86-64 -O
/usr/local/bin/bbl  
RUN chmod 755 /usr/local/bin/bbl  

