FROM ubuntu  
MAINTAINER Brian Antonelli  
  
ENV TERRAFORM_VERSION=0.11.1  
ENV TF_ALKS_PROVIDER_VERSION=0.9.11.1  
ENV TERRAGRUNT_VERSION=v0.13.23  
RUN apt-get update && \  
apt-get install -y \  
ca-certificates \  
wget \  
curl \  
unzip  
  
RUN mkdir /work  
VOLUME [ "/work" ]  
WORKDIR "/work"  
  
RUN wget -q -O /tmp/terraform.zip
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip /tmp/terraform.zip -d /usr/bin && \  
rm -rf /tmp/terraform.zip  
  
RUN wget -q -O tfalks.tar.gz https://github.com/Cox-Automotive/terraform-
provider-alks/releases/download/${TF_ALKS_PROVIDER_VERSION}/terraform-
provider-alks-linux-amd64.tar.gz && \  
tar -zxvf tfalks.tar.gz -C /usr/bin/ && \  
chmod a+x /usr/bin/terraform-provider-alks  
  
COPY .terraformrc /root/.terraformrc  
  
ADD https://github.com/gruntwork-
io/terragrunt/releases/download/${TERRAGRUNT_VERSION}/terragrunt_linux_amd64
/bin/terragrunt  
RUN chmod +x /bin/terragrunt  
  
ENTRYPOINT ["terraform"]  
CMD ["version"]  

