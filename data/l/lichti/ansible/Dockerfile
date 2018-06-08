FROM centos:centos7  
MAINTAINER Gustavo Lichti <gustavo.lichti@tricae.com.br>  
RUN yum clean all && \  
yum -y install epel-release && \  
yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-
paramiko python-setuptools git python-pip sshpass  
RUN mkdir /etc/ansible/  
RUN echo -e '[local]\nlocalhost' > /etc/ansible/hosts  
RUN pip install ansible==1.9.6  
  
ENV ANSIBLE_HOST_KEY_CHECKING False  
ENV ANSIBLE_SCP_IF_SSH y  
  
WORKDIR /ansible  

