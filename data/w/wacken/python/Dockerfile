FROM centos  
  
RUN yum install -y epel-release  
  
RUN yum update -y \  
&& yum install -y gcc wget make curl zlib-devel python-devel python-pip git  
  
RUN pip install -U pip \  
&& pip install -U setuptools

