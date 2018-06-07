FROM alpine:latest  
  
ENV TERRAFORM_VERSION=0.11.3  
ENV PACKER_VERSION=1.2.1  
ENV JQ_VERSION=1.5  
ADD
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
./  
ADD
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
./  
ADD https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-
linux64 /.  
  
RUN apk update && apk add ca-certificates curl && rm -rf /var/cache/apk/*  
COPY ./configure_aws_credential.sh /configure_aws_credential.sh  
  
RUN unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin && rm -f
terraform_${TERRAFORM_VERSION}_linux_amd64.zip  
RUN unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /bin && rm -f
packer_${PACKER_VERSION}_linux_amd64.zip  
RUN chmod +x jq-linux64 && mv jq-linux64 /bin/jq  

