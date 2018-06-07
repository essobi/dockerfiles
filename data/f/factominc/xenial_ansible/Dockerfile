FROM ubuntu:16.04  
  
MAINTAINER Mahesh Paolini-Subramanya <mahesh@dieswaytoofast.com>  
  
COPY Version.md .  
  
# Ansible and defaults  
RUN apt-get update -y && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install --no-install-recommends -yq \  
apt-transport-https \  
apt-utils \  
build-essential \  
ca-certificates \  
curl \  
git \  
libffi-dev \  
libssl-dev \  
python-pip \  
python-dev \  
python-yaml \  
libxml2-dev \  
libxslt1-dev \  
rsync \  
software-properties-common \  
zlib1g-dev && \  
apt-add-repository -y ppa:ansible/ansible && \  
apt-get update -y && \  
apt-get install -y ansible && \  
pip install --upgrade awscli \  
boto \  
boto3 \  
credstash \  
jinja2 \  
pycrypto \  
pyyaml \  
shyaml \  
\--ignore-installed six && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Docker client  
RUN curl -L -o /tmp/docker-17.06.0-ce.tgz
https://download.docker.com/linux/static/stable/x86_64/docker-17.06.0-ce.tgz
&& \  
tar -xz -C /tmp -f /tmp/docker-17.06.0-ce.tgz && \  
mv /tmp/docker/* /usr/bin  
  
RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh  

