FROM alpine:latest  
  
ENV TERRAFORM_VERSION "0.9.8"  
ENV TERRAFORM_COMMAND "plan"  
ENV ADDITIONAL_ARGUMENTS ""  
RUN apk add --update wget unzip ca-certificates && \  
wget
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin  
  
WORKDIR /data  
  
# No simple way to mix ENTRYPOINT with multiple pre-entry CMDs whilst also
specifying custom entrypoints args  
# So this is an unpleasant workaround using env vars  
CMD terraform init -force-copy && \  
terraform get && \  
terraform ${TERRAFORM_COMMAND} -no-color ${ADDITIONAL_ARGUMENTS}

