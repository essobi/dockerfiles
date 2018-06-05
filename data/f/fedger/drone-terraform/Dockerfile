FROM alpine:3.4  
ARG TERRAFORM_VERSION=0.7.11  
RUN apk --no-cache add \  
ca-certificates \  
jq \  
wget && \  
wget -qO /tmp/terraform.zip https://releases.hashicorp.com/terraform\  
/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
unzip /tmp/terraform.zip -d /usr/local/bin && \  
rm -rf /tmp/*  
  
COPY entrypoint.sh /usr/local/bin/drone-terraform  
ENTRYPOINT ["drone-terraform"]  

