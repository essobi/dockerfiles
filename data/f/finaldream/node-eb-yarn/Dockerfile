FROM node:6.9  
MAINTAINER Oliver Erdmann <o.erdmann@finaldream.de>  
  
# Install dependencies  
RUN apt-get update  
RUN apt-get -y install \  
python-pip \  
python-dev \  
build-essential \  
unzip \  
zip  
  
# Update pip and install eb cli  
RUN pip install -U pip  
# Fixes "ImportError: No module named packaging.version", see
https://github.com/Shippable/support/issues/3325  
RUN pip install -U setuptools==34.0.1  
RUN pip install --upgrade --user awsebcli  
ENV PATH "~/.local/bin:$PATH"  
# Install yarn  
RUN npm install --global yarn  

