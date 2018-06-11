From centos:7  
  
MAINTAINER Jimin Huang "huangjimin@whu.edu.cn"  
RUN yum update -y && \  
yum install python-devel git mariadb-devel gcc openssh openssh-clients -y && \  
curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install \--upgrade pip setuptools && \  
rm -r /root/.cache  
COPY requirements.txt ./  
  
RUN pip install -r requirements.txt  

