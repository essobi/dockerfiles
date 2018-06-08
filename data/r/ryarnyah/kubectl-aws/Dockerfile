FROM debian:8  
MAINTAINER Ryar Nyah <ryarnyah@gmail.com>  
  
LABEL CLOUD_PROVIDER aws  
LABEL COMPONENTS "kubectl,aws-cli,ansible,terraform,kops"  
LABEL VERSION stable  
  
ENV KOPS_VERSION 1.4.4  
ENV TERRAFORM_VERSION 0.8.4  
ENV ANSIBLE_VERSION 2.2.0.0  
ENV AWSCLI_VERSION 1.11.36  
ENV MARKUPSAFE_VERSION 0.23  
ENV CFFI_VERSION 0.8.6  
RUN apt-get update && \  
apt-get install -y curl python-pip python-dev groff unzip libffi-dev libyaml-
dev libssl-dev ca-certificates openssh-client && \  
dpkg -r python-pip && easy_install pip && \  
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s
https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && \  
chmod +x ./kubectl && \  
mv ./kubectl /usr/local/bin/kubectl && \  
curl -LO
https://github.com/kubernetes/kops/releases/download/v${KOPS_VERSION}/kops-
linux-amd64 && \  
chmod +x kops-linux-amd64 && \  
mv kops-linux-amd64 /usr/local/bin/kops && \  
curl -LO
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
chmod +x terraform && \  
mv ./terraform /usr/local/bin/terraform && \  
pip install --upgrade "awscli==${AWSCLI_VERSION}"
"ansible==${ANSIBLE_VERSION}" "markupsafe==${MARKUPSAFE_VERSION}"
"cffi==${CFFI_VERSION}" && \  
apt-get remove -y --purge curl && \  
apt-get autoremove -y --purge && \  
apt-get autoclean -y  

