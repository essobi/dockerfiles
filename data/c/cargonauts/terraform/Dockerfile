FROM hashicorp/terraform:0.7.13  
ENV TERRAFORM_PROVIDER_LOCALFILE_VERSION v0.1  
RUN apk add --update wget ca-certificates && \  
wget -q -O /bin/terraform-provider-localfile
"https://github.com/bennycornelissen/terraform-provider-
localfile/releases/download/${TERRAFORM_PROVIDER_LOCALFILE_VERSION}/terraform-
provider-localfile-linux-amd64" && \  
chmod +x /bin/terraform-provider-localfile && \  
apk del --purge wget ca-certificates && \  
rm -rf /var/cache/apk/*  

