FROM hashicorp/terraform:0.9.8  
MAINTAINER "James Powis <powisj@gmail.com>"  
ENV TERRAFORM_VERSION=0.9.8  
ENV TERRAGRUNT_VERSION=0.12.24  
ENV TERRAGRUNT_TFPATH=/bin/terraform  
  
RUN curl -sL https://github.com/gruntwork-
io/terragrunt/releases/download/v$TERRAGRUNT_VERSION/terragrunt_linux_386 \  
-o /bin/terragrunt && chmod +x /bin/terragrunt  
  
RUN apk add --update bash  
  
ENTRYPOINT []  

