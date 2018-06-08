# docker build --rm -t os-cli-centos7 .  
FROM lipcomputing/ansible-centos7  
MAINTAINER Mario David <mariojmdavid@gmail.com>  
LABEL description="Run Openstack CLI"  
  
RUN ansible-galaxy install LIP-Computing.ansible-role-os-cli && \  
ansible-playbook /etc/ansible/roles/LIP-Computing.ansible-role-os-
cli/tests/os-cli.yml  

