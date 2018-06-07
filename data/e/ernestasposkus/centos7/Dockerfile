FROM centos:centos7  
MAINTAINER Ernestas Poskus <hierco@gmail.com>  
RUN yum clean all && \  
yum -y install epel-release && \  
yum -y install iproute PyYAML python-jinja2 python-httplib2 python-keyczar
python-paramiko python-setuptools git python-pip  
  
# Install/prepare Ansible  
RUN mkdir -p /etc/ansible/  
RUN mkdir -p /opt/ansible/roles  
RUN printf '[local]\nlocalhost ansible_connection=local\n' >
/etc/ansible/hosts  
RUN pip install ansible  

