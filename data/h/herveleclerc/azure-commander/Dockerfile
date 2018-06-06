FROM ubuntu:16.04  
MAINTAINER <herve leclerc> herve.leclerc@alterway.fr  
#  
# This image install azure-cli, ansible, and powershell to drive efficiently
azure  
#  
  
ARG POWERSHELL_RELEASE=v6.0.0-alpha.14  
ARG POWERSHELL_PACKAGE=powershell_6.0.0-alpha.14-1ubuntu1.16.04.1_amd64.deb  
ARG POWERSHELL_HOME="/opt/microsoft/powershell/6.0.0-alpha.14"  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-add-repository -y ppa:ansible/ansible && \  
apt-get install -y --no-install-recommends \  
build-essential \  
nodejs \  
python-dev \  
python-pip \  
libxml2-dev \  
libxslt-dev \  
libssl-dev \  
libffi-dev \  
npm \  
ansible \  
libc6 \  
libcurl3 \  
ca-certificates \  
libgcc1 \  
libicu55 \  
libssl1.0.0 \  
libstdc++6 \  
libtinfo5 \  
libunwind8 \  
libuuid1 \  
zlib1g \  
curl \  
git && \  
ln -s /usr/bin/nodejs /usr/bin/node && \  
npm install -g azure-cli && \  
pip install --upgrade pip && \  
pip install -U setuptools && \  
pip install --upgrade ansible && \  
pip install azure==2.0.0rc5 && \  
rm -rf /var/lib/apt/lists/*  
  
  
# Install PowerShell package and clean up  
RUN curl -SLO
https://github.com/PowerShell/PowerShell/releases/download/$POWERSHELL_RELEASE/$POWERSHELL_PACKAGE
\  
&& dpkg -i $POWERSHELL_PACKAGE \  
&& rm $POWERSHELL_PACKAGE  
  
ENV PSHOME "$POWERSHELL_HOME"  
  
RUN powershell Install-Package -Force -Name AzureRM.NetCore.Preview -Source
https://www.powershellgallery.com/api/v2 -ProviderName NuGet -ExcludeVersion
-Destination $POWERSHELL_HOME/Modules  
  

