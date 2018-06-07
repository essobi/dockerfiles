FROM fedora:24  
MAINTAINER Rob Thijssen <rthijssen@gmail.com>  
  
RUN curl https://packages.microsoft.com/keys/microsoft.asc > ./microsoft.asc  
RUN rpm --import ./microsoft.asc  
RUN rpm -Uvh https://packages.microsoft.com/config/rhel/7/packages-microsoft-
prod.rpm  
RUN dnf update -y && dnf clean all  
RUN dnf install -y \  
git \  
gnupg2 \  
jq \  
nodejs \  
npm \  
powershell \  
pwgen \  
python \  
python-pip \  
unzip \  
uuid \  
&& dnf clean all  
RUN pip install --upgrade pip  
RUN pip install \  
awscli \  
boto3 \  
requests  
RUN npm install jsonlint -g  

