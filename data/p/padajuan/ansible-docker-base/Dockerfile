# Latest version of centos  
FROM centos:centos7  
MAINTAINER Juan Manuel Parrilla Madrid <jparrill@redhat.com>  
RUN yum clean all && \  
yum -y install epel-release && \  
yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-
paramiko python-setuptools git python-pip sshpass && \  
yum -y install gcc libffi-devel python-devel openssl-devel && \  
yum clean all && \  
mkdir /etc/ansible/ && \  
echo -e '[local]\nlocalhost' > /etc/ansible/hosts  
RUN pip install ansible==2.4.2 ansible-lint testinfra shade etcd molecule  

