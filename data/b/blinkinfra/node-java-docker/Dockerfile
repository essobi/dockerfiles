FROM node  
  
# Install packages needed for deployment  
RUN apt-get update && \  
apt-get install -y \  
\--no-install-recommends \  
ca-certificates \  
python3-dev \  
python3-pip \  
jq \  
unzip \  
ocaml \  
libelf-dev \  
&& rm -rf /var/lib/apt/lists/*  
RUN pip3 install awscli  
  
# Install nvm  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash  
ENV NVM_DIR="/home/node/.nvm"  
RUN mv /root/.nvm $NVM_DIR && chown -R node:node $NVM_DIR  
  
# Wrap nvm into a script  
RUN /bin/echo -e '#! /bin/bash\n\  
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"\n\  
nvm $@'\  
>> /bin/nvm  
RUN chmod 0755 /bin/nvm  
  
# Install Docker (for remote builds)  
RUN set -x &&\  
VER="latest" &&\  
curl -L -o /tmp/docker-$VER.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz &&\  
tar -xz -C /tmp -f /tmp/docker-$VER.tgz &&\  
mv /tmp/docker/* /usr/bin  
  
# Install Terraform  
ENV TERRAFORM_VERSION=0.10.6  
RUN curl -o terraform.zip
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip terraform.zip -d /usr/bin && rm -f terraform.zip  
  
# Install Java  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu
xenial main" && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  

