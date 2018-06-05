FROM ubuntu:16.04  
LABEL maintainer="Valerie Parham-Thompson"  
LABEL contact="valerie@tortugatech.com"  
LABEL version="2017-02"  
  
#this dockerfile originally created from example at  
#https://medium.com/@pcarion/a-consul-a-vault-and-a-docker-walk-into-a-
bar-d5a5bf897a87  
ENV VAULT_VERSION 0.7.0  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
git \  
curl \  
wget \  
vim \  
net-tools \  
iputils-ping \  
dnsutils \  
zip \  
unzip \  
mysql-client \  
ansible \  
percona-toolkit \  
python-pip \  
ant \  
default-jre \  
&& wget -O /tmp/vault.zip
"https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip"
\  
&& unzip -d /bin /tmp/vault.zip \  
&& chmod 755 /bin/vault \  
&& rm /tmp/vault.zip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/riptano/ccm.git  
  
RUN pip install psutil  
  
VOLUME "/mnt/data"  
CMD ["/bin/bash"]

