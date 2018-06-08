# docker build --rm -t os-cli-ubuntu16.04 .  
FROM lipcomputing/ansible-ubuntu16.04  
MAINTAINER Mario David <mariojmdavid@gmail.com>  
LABEL description="Run Openstack CLI"  
  
RUN ansible-galaxy install LIP-Computing.ansible-role-os-cli && \  
ansible-playbook /root/.ansible/roles/LIP-Computing.ansible-role-os-
cli/tests/os-cli.yml  

