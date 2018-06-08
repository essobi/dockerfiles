FROM centos:6  
RUN rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6 \  
&& yum install -y epel-release  
  
RUN yum install -y \  
git \  
python-pep8 \  
python-setupdocs \  
python-setuptools \  
rpm-build \  
&& yum clean all  
  

