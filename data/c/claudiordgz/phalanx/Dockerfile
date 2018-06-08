FROM node:carbon-alpine  
LABEL maintainer "Claudio Rodriguez <claudio.rdgz@gmail.com>"  
  
ENV TERRAFORM_VERSION=0.11.7  
WORKDIR /data  
  
RUN apk add --update --no-cache zip ca-certificates openssl && \  
wget -O terraform.zip
"https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip"
&& \  
unzip terraform.zip -d /bin && \  
rm -rf /var/cache/apk/* && \  
rm -f terraform.zip  
  
ENTRYPOINT ["sh"]  

