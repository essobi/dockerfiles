FROM alpine:3.6  
LABEL name="terraform"  
LABEL version=0.9.11  
LABEL maintainer="Stephane Jourdan <fasten@fastmail.fm>"  
MAINTAINER Stephane Jourdan <fasten@fastmail.fm>  
ENV TERRAFORM_VERSION=0.9.11  
VOLUME ["/data"]  
WORKDIR /data  
RUN apk --update --no-cache add ca-certificates openssl sudo && \  
wget -O terraform.zip
"https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip"
&& \  
unzip terraform.zip -d /bin && \  
rm -rf terraform.zip /var/cache/apk/*  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["--help"]  

