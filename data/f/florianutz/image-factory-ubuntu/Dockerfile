FROM ubuntu:16.04  
MAINTAINER "Florian Utz"  
  
ENV PACKER_VERSION=1.1.3  
ENV
PACKER_SHA256SUM=b7982986992190ae50ab2feb310cb003a2ec9c5dcba19aa8b1ebb0d120e8686f  
####  
RUN echo "===> Install packages ..." && \  
apt update && apt upgrade -y && \  
apt install -y python3 python-pip openssl ca-certificates sudo groff \  
python-dev libffi-dev libssl-dev build-essential \  
git wget openssl curl jq unzip && \  
pip install --no-cache-dir --upgrade pip cffi && \  
\  
echo "===> Installing Ansible..." && \  
pip install --no-cache-dir --upgrade ansible && \  
\  
echo "===> Installing awscli..." && \  
pip install --no-cache-dir --upgrade awscli && \  
\  
echo "===> Cleanup" && \  
apt clean all && \  
echo "===> Package installation completed!"  
  
COPY setup-packer.sh /usr/local/bin/  
RUN /usr/local/bin/setup-packer.sh  
  
RUN useradd -m imagefactory && mkdir /data && chown imagefactory:imagefactory
/data && chmod 770 /data  
USER imagefactory  
WORKDIR /data  
###  
ENTRYPOINT ["/bin/bash"]  

