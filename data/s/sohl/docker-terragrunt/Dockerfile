FROM hashicorp/terraform:0.9.5  
MAINTAINER Serge Ohl <sohl@coveo.com>  
  
ARG TERRAGRUNT_VERSION=0.12.18.02  
ARG TERRAGRUNT_TFPATH=/bin/terraform  
  
RUN curl -sL
https://github.com/coveo/terragrunt/releases/download/v$TERRAGRUNT_VERSION/terragrunt_linux_amd64
-o /bin/terragrunt && chmod +x /bin/terragrunt  

