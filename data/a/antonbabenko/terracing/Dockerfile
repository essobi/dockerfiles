FROM ubuntu:16.04  
MAINTAINER "Anton Babenko <anton@antonbabenko.com>"  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
apt-utils bash-completion \  
apt-transport-https software-properties-common python-software-properties \  
software-properties-common python-software-properties \  
curl wget git tar gzip zip unzip ca-certificates openssh-client vim-tiny nano
jq python make tree && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
# Install AWS CLI  
RUN curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py && \  
python /tmp/get-pip.py && \  
pip install awscli && \  
rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Don't move these arguments higher because it will build images slower  
ARG TERRAFORM_VERSION=0.11.7  
ARG TERRAGRUNT_VERSION=0.14.7  
ARG TFLINT_VERSION=0.5.4  
# Install Terraform  
RUN curl -sL
https://releases.hashicorp.com/terraform/"$TERRAFORM_VERSION"/terraform_"$TERRAFORM_VERSION"_linux_amd64.zip
-o terraform_"$TERRAFORM_VERSION"_linux_amd64.zip && \  
unzip terraform_"$TERRAFORM_VERSION"_linux_amd64.zip -d /usr/bin && \  
rm -rf terraform_"$TERRAFORM_VERSION"_linux_amd64.zip && \  
chmod +x /usr/bin/terraform  
  
# Install Terragrunt  
RUN curl -sL https://github.com/gruntwork-
io/terragrunt/releases/download/v"$TERRAGRUNT_VERSION"/terragrunt_linux_amd64
-o /usr/bin/terragrunt && \  
chmod +x /usr/bin/terragrunt  
  
# Install tflint  
RUN curl -sL
https://github.com/wata727/tflint/releases/download/v"$TFLINT_VERSION"/tflint_linux_amd64.zip
-o tflint_linux_amd64.zip && \  
unzip tflint_linux_amd64.zip -d /usr/bin && \  
rm -rf tflint_linux_amd64.zip && \  
chmod +x /usr/bin/tflint  
  
# Copy Terracing helper scripts  
COPY scripts /usr/local/bin/  
RUN chmod +x /usr/local/bin/*  
  
CMD ["/usr/bin/terragrunt"]

