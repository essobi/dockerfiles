FROM alpine:3.6  
MAINTAINER Lorelei Aurora <iam@l5i.me>  
  
ENV TERRAFORM_VERSION 0.9.4  
RUN apk --update --no-cache add ca-certificates openssl sudo && \  
wget -O terraform.zip
"https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip"
&& \  
unzip terraform.zip -d /usr/bin && \  
rm -rf terraform.zip  
  
VOLUME ["/data"]  
WORKDIR /data  
  
ENTRYPOINT ["/usr/bin/terraform"]  
  
CMD ["--help"]  

