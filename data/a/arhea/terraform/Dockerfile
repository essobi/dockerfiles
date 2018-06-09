FROM alpine:latest  
  
ENV TERRAFORM_VERSION=0.10.0-rc1  
ENV
TERRAFORM_SHA256SUM=66820a4d12c25a6d0c83dd877d308aa0c8fce11ce63072f5753167e917464770  
  
RUN apk add --update git curl openssh \  
&& curl
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
> terraform_${TERRAFORM_VERSION}_linux_amd64.zip \  
&& echo "${TERRAFORM_SHA256SUM}
terraform_${TERRAFORM_VERSION}_linux_amd64.zip" >
terraform_${TERRAFORM_VERSION}_SHA256SUMS \  
&& sha256sum -cs terraform_${TERRAFORM_VERSION}_SHA256SUMS \  
&& unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin \  
&& rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip  
  
ENTRYPOINT ["/bin/terraform"]  

