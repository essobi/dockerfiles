FROM centos:7  
  
ENV ANSIBLE_VERSION=2.2.1.0 \  
ANSIBLE_UID=555  
  
RUN yum -y install epel-release yum-plugin-ovl deltarpm && \  
yum -y update && \  
yum -y install curl \  
dnsutils \  
git \  
less \  
openssl \  
python-httplib2 \  
python-jinja2 \  
python-keyczar \  
python-paramiko \  
python-pip \  
python-setuptools \  
PyYAML \  
ssh \  
sudo \  
vim-minimal && \  
pip install --upgrade pip && \  
pip install ansible==${ANSIBLE_VERSION} && \  
ansible --version && \  
groupadd -g ${ANSIBLE_UID} -r ansible && \  
useradd -u ${ANSIBLE_UID} -r -g ansible ansible && \  
mkdir /code && \  
mkdir /home/ansible && chown -R ansible: /home/ansible  
  
USER ansible  
WORKDIR /code  
  
RUN ansible --version  
  
ENTRYPOINT [ "/usr/bin/ansible-playbook" ]  

