# Docker image of Ansible with patches applied to it  
# --------------------------------------------------  
FROM ansible/centos7-ansible:devel  
MAINTAINER Misho Krastev <misho.kr@gmail.com>  
  
# Git configuration  
RUN git config --global user.email "you@example.com" && \  
git config --global user.name "Your Name"  
  
# Ansible installation folder  
WORKDIR /opt/ansible/ansible  
  
# 1. Patches to apply to ansible/ansible  
# https://github.com/ansible/ansible/pull/9281  
RUN git remote add patch https://github.com/woltage/ansible.git && \  
git fetch -q patch && \  
git checkout -b patched patch/devel && \  
git rebase devel && \  
git checkout devel && \  
git merge patched  
  
# 2. Patches to apply to ansible/ansible-modules-core  
# https://github.com/ansible/ansible-modules-core/pull/153  
WORKDIR /opt/ansible/ansible/lib/ansible/modules/core  
RUN git remote add patch https://github.com/woltage/ansible-modules-core.git
&& \  
git fetch -q patch && \  
git checkout -b patched patch/devel && \  
git rebase devel && \  
git checkout devel && \  
git merge patched  
  
# 2B. Patches to apply to ansible/ansible-modules-core (v2)  
# https://github.com/ansible/ansible-modules-core/pull/153  
WORKDIR /opt/ansible/ansible/v2/ansible/modules/core  
RUN git remote add patch https://github.com/woltage/ansible-modules-core.git
&& \  
git fetch -q patch && \  
git checkout -b patched patch/devel && \  
git rebase devel && \  
git checkout devel && \  
git merge patched  
  
# default location for playbook  
RUN mkdir /playbook  
WORKDIR /playbook  

