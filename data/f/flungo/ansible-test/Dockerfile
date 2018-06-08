FROM flungo/ansible:archlinux  
  
# Install sudo  
RUN pacman -Syyu --noconfirm sudo  
  
# Setup the build arguments  
ARG ansible_user=ansible  
ARG ansible_directory=/usr/src/ansible  
ARG ansible_playbook=test/main.yml  
  
# Persist the build arguments  
ENV ANSIBLE_USER=${ansible_user} \  
ANSIBLE_DIRECTORY=${ansible_directory} \  
ANSIBLE_PLAYBOOK=${ansible_playbook}  
# Setup the Ansible playbook directory  
WORKDIR ${ANSIBLE_DIRECTORY}  
# Create the test user and add them to the sudoers  
RUN useradd -m -s /bin/bash ${ansible_user}  
RUN ansible localhost -m lineinfile -a "dest=/etc/sudoers state=present
regexp='^${ansible_user}' line='${ansible_user} ALL=(ALL) NOPASSWD: ALL'"  
USER ${ansible_user}  
# Test the ansible project onbuild  
ONBUILD COPY . ${ANSIBLE_DIRECTORY}  
ONBUILD RUN ansible-playbook -v ${ANSIBLE_PLAYBOOK} \--syntax-check  
ONBUILD RUN ansible-playbook -v ${ANSIBLE_PLAYBOOK}  

