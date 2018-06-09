# docker build -t beagle/caravel-python-npm-base:1.0 -f Dockerfile-all .  
FROM centos:7.2.1511  
MAINTAINER xjw <xingjw@beagledata.com>  
# COPY Centos-7.repo /etc/yum.repos.d/CentOS-Base.repo  
RUN yum -y install epel-release \  
&& yum -y update \  
&& yum -y install python-pip gcc gcc-c++ cpp make openssl openssl-devel
python-devel nodejs npm git unzip libffi-devel python-devel python-pip python-
wheel openssl-devel libsasl2-devel openldap-devel\  
&& yum clean all  
RUN pip install --upgrade pip \  
&& pip install virtualenv \  
&& cd /root/ \  
&& git clone https://github.com/airbnb/superset.git  
  
  
  

