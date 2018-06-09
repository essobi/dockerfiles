FROM alpine:3.3  
ENV TERRAFORM_VERSION 0.11.2  
# Install curl  
RUN apk add --update curl && rm -rf /var/cache/apk/*  
  
# Install Terraform.  
RUN apk add --update unzip ca-certificates \  
&& mkdir -p /opt/terraform \  
&& wget -O /opt/terraform.zip
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_386.zip
\  
&& unzip -d /opt/terraform /opt/terraform.zip \  
&& rm /opt/terraform.zip \  
&& apk del unzip \  
&& rm -rf /var/cache/apk/*  
  
# Add global terraform configs.  
COPY ./terraplan-global /opt/terraplan-global  
  
# Set entrypoint.  
COPY ./entrypoint /opt/entrypoint  
RUN chmod +x /opt/entrypoint  
ENTRYPOINT ["/opt/entrypoint"]  
  
CMD ["show"]  

