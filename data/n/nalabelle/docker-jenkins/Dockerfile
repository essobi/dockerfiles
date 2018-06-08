FROM jenkins/jenkins:alpine  
USER root  
RUN \  
echo "*** adding additional packages ***" && \  
apk add \--no-cache \  
ansible \  
build-base \  
git \  
libffi-dev \  
openssl-dev \  
python-dev \  
py-virtualenv && \  
pip install \  
proxmoxer \  
requests \  
&& \  
echo "*** done ***"  
USER jenkins  

