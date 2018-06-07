FROM amazonlinux:latest  
  
RUN yum install -v -y gcc \  
gcc-c++ \  
zip \  
python36-setuptools \  
sudo \  
wget \  
unzip \  
git  
  
RUN easy_install-3.6 pip  
  
RUN pip3 install --upgrade awscli boto3 virtualenv  
  
RUN export PATH=~/.local/bin:$PATH  
  
RUN mkdir -p /usr/local/src  
  
RUN sudo yum -y install jq  
  
RUN wget
https://releases.hashicorp.com/terraform/0.10.8/terraform_0.10.8_linux_amd64.zip
\  
-O /usr/local/src/terraform.zip  
  
RUN cd /usr/local/src && unzip terraform.zip && mv terraform /usr/local/bin  
  
RUN wget
https://releases.hashicorp.com/vault/0.8.3/vault_0.8.3_linux_amd64.zip \  
-O /usr/local/src/vault.zip  
  
RUN cd /usr/local/src && unzip vault.zip && mv vault /usr/local/bin  

