FROM ubuntu:14.04  
MAINTAINER Prasath Soosaithasan <prasath.soosaithasan@gmail.com>  
  
# 1) Install Ansible in a Docker container (stolen from
ansible/ubuntu14.04-ansible)  
# --------------------------------------------------  
RUN apt-get -y update && \  
apt-get install -y python-yaml python-jinja2 python-httplib2 python-keyczar
python-paramiko python-setuptools python-pkg-resources git python-pip  
RUN mkdir /etc/ansible/  
RUN mkdir /opt/ansible/  
RUN git clone http://github.com/ansible/ansible.git /opt/ansible/ansible  
WORKDIR /opt/ansible/ansible  
RUN git submodule update --init  
ENV PATH /opt/ansible/ansible/bin:/bin:/usr/bin:/sbin:/usr/sbin  
ENV PYTHONPATH /opt/ansible/ansible/lib  
ENV ANSIBLE_LIBRARY /opt/ansible/ansible/library  
  
# 2) Run an Ansible script to provision the container  
# --------------------------------------------------  
ADD ansible /etc/ansible  
WORKDIR /etc/ansible  
RUN ansible-playbook provision-container.yml  
  
# 3) Execute some Docker-specific commands that are not available via Ansible  
# --------------------------------------------------  
# 3.1) volumes  
# No volumes  
# 3.2) ports  
EXPOSE 80 443  
# 4) CMD Start PID 1 process  
# --------------------------------------------------  
CMD ["nginx", "-g", "daemon off;"]

