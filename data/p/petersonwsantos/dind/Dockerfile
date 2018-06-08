FROM ubuntu:16.04  
  
LABEL maintainer="peterson W Santos <opeterson@hotmail.com>"  
LABEL tag="1.0"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qqy && apt-get install -qqy \  
curl \  
gcc \  
python-dev \  
python-setuptools \  
apt-transport-https \  
lsb-release \  
openssh-client \  
git \  
vim \  
apt-utils \  
ca-certificates curl \  
software-properties-common && \  
curl -fsSL "https://download.docker.com/linux/ubuntu/gpg" | apt-key add -qq &&
\  
echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial edge" >
/etc/apt/sources.list.d/docker.list && \  
apt-get update -qq && \  
apt-get install -y -qq --no-install-recommends docker-ce && \  
apt-get install -f && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/*  

