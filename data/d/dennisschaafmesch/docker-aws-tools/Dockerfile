FROM golang:1.9-alpine3.6  
RUN apk add --no-cache \  
bash \  
coreutils \  
curl \  
git \  
gnupg \  
make \  
ncurses \  
nodejs \  
nodejs-npm \  
perl \  
python \  
unzip \  
wget \  
zip  
  
WORKDIR /tmp  
  
# Install jsonlint  
RUN curl --silent --location --output jsonlint.tar.gz
https://github.com/dmeranda/demjson/archive/release-2.2.4.tar.gz && \  
tar -xvf jsonlint.tar.gz && \  
cd demjson-release-2.2.4 && \  
python setup.py install  
  
# Install colordiff  
ENV COLORDIFF_VERSION=1.0.18  
RUN curl --silent --output colordiff.tar.gz
"https://www.colordiff.org/colordiff-${COLORDIFF_VERSION}.tar.gz" && \  
curl --silent --output colordiff.tar.gz.sig
"https://www.colordiff.org/colordiff-${COLORDIFF_VERSION}.tar.gz.sig" && \  
curl --silent --output colordiff-author-public-key
https://www.sungate.co.uk/gpgkey_2013.txt && \  
gpg --import colordiff-author-public-key && \  
gpg --verify colordiff.tar.gz.sig colordiff.tar.gz && \  
tar -xvf colordiff.tar.gz && \  
cd colordiff-${COLORDIFF_VERSION} && \  
make install  
  
# Install jq  
RUN curl --silent --location --output /usr/local/bin/jq
https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 && \  
chmod ug+x /usr/local/bin/jq  
  
# Install AWS CLI Client  
RUN curl --silent --output awscli-bundle.zip "https://s3.amazonaws.com/aws-
cli/awscli-bundle.zip" && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
  
# Install Terraform  
# Use Terraform Bundle to create a bundle with commonly used provider plugins  
# This is so we do not have to download provider plugins on every Terraform
run  
ENV TERRAFORM_HOME=$GOPATH/src/github.com/hashicorp/terraform  
ADD terraform-bundle.hcl /tmp/terraform-bundle.hcl  
RUN git clone https://github.com/hashicorp/terraform.git ${TERRAFORM_HOME} &&
\  
cd ${TERRAFORM_HOME} && \  
go install ./tools/terraform-bundle && \  
terraform-bundle package /tmp/terraform-bundle.hcl && \  
mkdir distribution && \  
cd distribution && \  
unzip $(find ../ -name terraform_*.zip) -d /usr/local/bin && \  
rm -rf ${TERRAFORM_HOME}  
  
# Install Packer  
ENV PACKER_VERSION=0.12.3  
RUN curl --silent --output packer.zip
"https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip"
&& \  
unzip -d /usr/local/bin/ packer.zip  
  
CMD [ "bash" ]  

