FROM microsoft/dotnet:2-sdk  
  
LABEL maintainer="alberto.mardomingo@masmovil.com"  
  
RUN apt-get update && \  
apt-get install -y \  
python-pip \  
python-dev \  
build-essential \  
gettext \  
sudo  
  
# For some reason, we also need npm and a bunch of other stuffs.  
RUN curl -sL -o /tmp/node.sh https://deb.nodesource.com/setup_8.x && \  
bash /tmp/node.sh && sudo apt-get install -y nodejs && \  
npm install \--global webpack@2.5.1  
  
RUN pip install awscli==1.11.76  
  
# Install Kubectl  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && \  
mv kubectl /bin/kubectl && \  
chmod +x /bin/kubectl  

