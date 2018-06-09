FROM debian:jessie-slim  
  
# Install required base packages  
RUN apt-get update && apt-get install -y \  
git \  
python-minimal \  
python-setuptools \  
python-pip \  
python-paramiko \  
python-jinja2 \  
python-dev \  
libffi-dev \  
libssl-dev \  
build-essential  
  
# Upgrade pip  
RUN pip install --upgrade pip  
  
# Install ansible  
RUN pip install --no-cache-dir ansible  
  
# Cleanup  
RUN apt-get purge -y -f --force-yes \  
python-dev \  
build-essential \  
libssl-dev \  
libffi-dev  

