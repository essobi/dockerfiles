FROM centos:7  
RUN yum install -y epel-release  
RUN yum install -y python-pip gcc gcc-c++ kernel-devel python-devel libxslt-
devel libffi-devel openssl-devel krb5-workstation  
  
RUN mkdir /ansible  
COPY ansible.cfg /etc/ansible/ansible.cfg  
COPY requirements.txt /ansible/requirements.txt  
WORKDIR /ansible  
RUN pip install -r requirements.txt  
COPY ansible.cfg /etc/ansible/ansible.cfg  

