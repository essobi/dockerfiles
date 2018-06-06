FROM python:3.6.4  
MAINTAINER Jamie Alessio <jamie@calthorpeanalytics.com>  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
git \  
libxml2-dev \  
libxslt1-dev \  
nodejs \  
ruby \  
ruby-dev \  
shellcheck \  
unzip \  
zlib1g-dev  
  
RUN mkdir -p /tmp/terraform && \  
cd /tmp/terraform && \  
curl -# -o terraform.zip
https://releases.hashicorp.com/terraform/0.9.11/terraform_0.9.11_linux_amd64.zip
&& \  
unzip terraform.zip && \  
mv terraform /usr/local/bin && \  
rm -rf /tmp/terraform  
  
RUN pip install pre-commit==1.4.5  
  
RUN mkdir /pre-commit  
COPY .pre-commit-config-for-build.yaml /pre-commit/.pre-commit-config.yaml  
  
# Use pre-generated .pre-commit-config.yaml to run pre-commit python  
# executable so all dependencies are automatically installed in image.  
RUN cd /pre-commit && \  
git init . && \  
cat .pre-commit-config.yaml && \  
pre-commit run  
  
ENTRYPOINT ["pre-commit"]  

