FROM ubuntu:14.04  
MAINTAINER Halvor Granskogen Bjørnstad <halvor@hoopla.no>  
RUN sudo apt-get update && \  
sudo apt-get -y upgrade && \  
sudo apt-get install -y libssl-dev && \  
sudo apt-get -y install python2.7 swig libpq-dev python-dev libffi-dev wget
curl libxml2-dev libxslt1-dev vim && \  
wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py && \  
python /tmp/get-pip.py && \  
pip install sh logging setuptools awscli && \  
  
# wkhtmltopdf  
apt-get install -y xz-utils libxrender1 libfontconfig1 libXext6 && \  
wget http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-
generic-amd64.tar.xz && \  
unxz wkhtmltox-0.12.3_linux-generic-amd64.tar.xz && \  
tar -xf wkhtmltox-0.12.3_linux-generic-amd64.tar && \  
mv /wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf && \  
rm -rf /wkhtmltox && \  
rm -rf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz && \  
  
cd /usr/include/openssl/ && \  
sudo ln -s ../x86_64-linux-gnu/openssl/opensslconf.h . && \  
pip install virtualenv \--upgrade && \  
mkdir /virtualenvs && \  
virtualenv /virtualenvs/hoopla && \  
  
#clean apt-cache  
rm -rf /var/lib/apt/lists/*  

