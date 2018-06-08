FROM centos:7  
  
RUN rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7 \  
&& yum install -y epel-release  
  
RUN yum install -y \  
git \  
numpy \  
python-coverage \  
python-pep8 \  
python-pip \  
python-setupdocs \  
python-setuptools \  
python2-pylint \  
python2-pytest-cov \  
rpm-build \  
&& yum clean all  
  

