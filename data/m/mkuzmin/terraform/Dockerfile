FROM alpine:3.4  
ARG TERRAFORM_VERSION=0.9.1  
ARG VMWARE_VERSION=1.2  
ARG KAPACITOR_VERSION=0.3  
RUN apk update && \  
apk add ca-certificates wget git && \  
update-ca-certificates && \  
wget -nv
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
-O terraform.zip && \  
unzip terraform.zip -d /usr/local/bin/ && \  
rm terraform.zip && \  
wget -nv https://github.com/mkuzmin/terraform-provider-
vmware/releases/download/v${VMWARE_VERSION}/terraform-provider-vmware.linux -O
/usr/local/bin/terraform-provider-vmware && \  
wget -nv https://github.com/mkuzmin/terraform-provider-
kapacitor/releases/download/v${KAPACITOR_VERSION}/terraform-provider-
kapacitor.linux -O /usr/local/bin/terraform-provider-kapacitor && \  
chmod +x /usr/local/bin/terraform-provider-*  
  
ENTRYPOINT ["terraform"]  

