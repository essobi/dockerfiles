FROM amazonlinux  
MAINTAINER Yasushi Kobayashi <ptpadan@gmail.com>  
RUN yum -y update && \  
yum -y install gcc openssl openssl-devel libffi-devel && \  
yum -y install python27 python27-pip python27-devel python27-crypto
python27-libs python27-setuptools && \  
curl "https://bootstrap.pypa.io/get-pip.py" -o get-pip.py && \  
python get-pip.py && \  
pip install -U pip && \  
pip install cryptography && \  
pip install ansible  

