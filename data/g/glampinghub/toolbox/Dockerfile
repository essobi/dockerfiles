FROM ubuntu:latest  
MAINTAINER José Luis Salvador Rufo <salvador.joseluis@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 /usr/bin/confd  
ADD https://deb.nodesource.com/setup_6.x /tmp/nodesource_setup.sh  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections && \  
bash /tmp/nodesource_setup.sh && \  
apt-get install --no-install-recommends -qy \  
openssh-client \  
git \  
openssl \  
curl \  
ca-certificates \  
build-essential \  
python-pip python-dev python-setuptools groff \  
tmux docker.io \  
nodejs && \  
pip install awscli && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
chmod +x /usr/bin/confd  

