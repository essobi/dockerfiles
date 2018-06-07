FROM phase2/servicebase:latest  
  
ENV TERRAFORM_VERSION=0.6.12 \  
PATH="/opt/terraform:${PATH}" \  
TERRAFORM_UID=555  
RUN yum -y install unzip && \  
mkdir -p /opt/terraform && \  
mkdir -p /code && \  
groupadd -g ${TERRAFORM_UID} -r terraform && \  
useradd -u ${TERRAFORM_UID} -r -g terraform terraform && \  
cd /opt/terraform && \  
curl -O
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip  
  
USER terraform  
WORKDIR /code  
  
ENTRYPOINT ["/opt/terraform/terraform"]  

