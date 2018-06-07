FROM alpine:3.6  
ARG TERRAFORM_VERSION=0.9.11  
ARG AWS_VERSION=1  
ARG VMWARE_VERSION=1.2  
ARG KAPACITOR_VERSION=0.3  
RUN apk add --no-cache ca-certificates wget git mariadb-client && \  
update-ca-certificates && \  
wget -nv
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
-O /tmp/terraform.zip && \  
unzip /tmp/terraform.zip -d /usr/local/bin/ && \  
rm /tmp/terraform.zip && \  
wget -nv https://github.com/jetbrains-infra/terraform-provider-
aws/releases/download/${AWS_VERSION}/terraform-provider-aws.linux -O
/usr/local/bin/terraform-provider-aws && \  
wget -nv https://github.com/mkuzmin/terraform-provider-
vmware/releases/download/v${VMWARE_VERSION}/terraform-provider-vmware.linux -O
/usr/local/bin/terraform-provider-vmware && \  
wget -nv https://github.com/mkuzmin/terraform-provider-
kapacitor/releases/download/v${KAPACITOR_VERSION}/terraform-provider-
kapacitor.linux -O /usr/local/bin/terraform-provider-kapacitor && \  
chmod +x /usr/local/bin/terraform-provider-*  
  
ENTRYPOINT ["terraform"]  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/jetbrains-infra/docker-image-
terraform.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0"  

