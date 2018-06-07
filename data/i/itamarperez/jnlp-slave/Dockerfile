FROM adriagalin/jenkins-jnlp-slave  
  
# Update system  
RUN apt-get update  
  
# Install and Test PHP  
RUN apt-get install --force-yes --no-install-recommends -yq python-pip jq \  
&& pip install -q awscli  
  
RUN curl -L
https://releases.hashicorp.com/packer/1.1.3/packer_1.1.3_linux_amd64.zip -o
/tmp/packer.zip; unzip /tmp/packer.zip -d /usr/local/bin  
RUN curl -L
https://releases.hashicorp.com/terraform/0.11.3/terraform_0.11.3_linux_amd64.zip
-o /tmp/terraform.zip; unzip /tmp/terraform.zip -d /usr/local/bin  
RUN curl -L https://github.com/gruntwork-
io/terragrunt/releases/download/v0.14.0/terragrunt_linux_amd64 -o
/usr/local/bin/terragrunt && chmod +x /usr/local/bin/terragrunt  
RUN curl -L https://storage.googleapis.com/kubernetes-
release/release/v1.8.0/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl &&
chmod +x /usr/local/bin/kubectl  
  
# Tidy up  
RUN apt-get -y autoremove && apt-get clean && apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

