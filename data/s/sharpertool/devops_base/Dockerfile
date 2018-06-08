FROM circleci/python:3.6.1  
ARG PACKER_VERSION=1.1.0  
ARG
PACKER_CHECKSUM=bd1eddfa114f7e6258ef3419613380297f1b4e438f5bae92f1177150519be934  
ARG TERRAFORM_VERSION=0.10.7  
ARG
TERRAFORM_CHECKSUM=804d31cfa5fee5c2b1bff7816b64f0e26b1d766ac347c67091adccc2626e16f3  
ARG TERRAGRUNT_URL=https://github.com/gruntwork-
io/terragrunt/releases/download/v0.13.7/terragrunt_linux_amd64  
  
ARG H=/home/circleci  
  
#
https://releases.hashicorp.com/terraform/0.9.11/terraform_0.9.11_linux_amd64.zip  
RUN echo "alias ll='ls -alh'" >> ${H}/.bashrc && echo "set -o vi" >>
${H}/.bashrc  
  
# Install packer  
#
https://releases.hashicorp.com/packer/1.1.0/packer_1.1.0_linux_amd64.zip?_ga=2.68833042.2067967940.1507403368-479016542.1503958022  
RUN wget -O /tmp/packer.zip
"https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip";
\  
echo "${PACKER_CHECKSUM} /tmp/packer.zip" | sha256sum --check - ; \  
sudo unzip -oud "/usr/local/bin" /tmp/packer.zip; \  
rm /tmp/packer.zip  
  
# Install terraform  
RUN echo "Installing Terraform"; \  
wget -O /tmp/terraform.zip
"https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip";
\  
echo "${TERRAFORM_CHECKSUM} /tmp/terraform.zip" | sha256sum --check - ; \  
sudo unzip -oud "/usr/local/bin" /tmp/terraform.zip; \  
rm /tmp/terraform.zip  
  
# Install Terragrunt  
RUN sudo wget -O "/usr/local/bin/terragrunt" "${TERRAGRUNT_URL}" ; \  
sudo chmod +x /usr/local/bin/terragrunt  
  
# Install jq  
RUN sudo wget -O "/usr/local/bin/jq"
"https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64"; \  
sudo chmod +x /usr/local/bin/jq  
  
RUN sudo pip install ansible awscli  
  
# Install nodejs 6.x and npm and yarn, needed to compile assets  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN sudo apt-get install -y nodejs  
RUN sudo npm install -g yarn@latest yuglify@latest  
  
RUN sudo apt-get install rsync  
  
RUN sudo /bin/bash -c 'sudo curl -L
https://github.com/docker/compose/releases/download/1.17.0/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose'  
RUN sudo chmod +x /usr/local/bin/docker-compose  
  
RUN curl -sL https://sentry.io/get-cli/ | bash  
  
ADD build_container.bashrc /home/circleci/.bashrc  

