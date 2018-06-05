FROM centos:6  
RUN yum install -y centos-release-scl  
RUN yum install -y python27-python-pip python27-python-devel openssl-devel
libffi-devel gcc  
RUN scl enable python27 "pip install --upgrade pip setuptools"  
RUN scl enable python27 "pip install ansible testinfra"  
ADD "inventory.conf" "/etc/ansible/hosts"  

