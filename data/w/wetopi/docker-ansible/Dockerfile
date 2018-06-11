# Dockerfile for building Ansible image for Alpine 3, with as few additional
software as possible.  
#  
# @see https://bitbucket.org/wetopi/docker-ansible  
#  
#  
# pull base image  
FROM docker:18.03.0-ce  
  
MAINTAINER Joan Vega <joan@wetopi.com>  
  
  
RUN echo "===> Installing curl and sudo to emulate normal OS behavior..." && \  
apk --update add sudo curl && \  
\  
\  
echo "===> Adding Python runtime..." && \  
apk --update add python py-pip openssl ca-certificates && \  
apk --update add --virtual build-dependencies \  
python-dev libffi-dev openssl-dev build-base && \  
pip install --upgrade pip cffi && \  
\  
\  
echo "===> Installing Ansible..." && \  
pip install ansible && \  
\  
\  
echo "===> Installing handy tools (not absolutely required)..." && \  
pip install --upgrade pywinrm && \  
apk --update add sshpass openssh-client rsync git && \  
\  
\  
echo "===> Removing package list..." && \  
apk del build-dependencies && \  
rm -rf /var/cache/apk/* && \  
\  
\  
echo "===> Adding hosts for convenience..." && \  
mkdir -p /etc/ansible && \  
echo 'localhost' > /etc/ansible/hosts  
  
  
# default command: display Ansible version  
CMD [ "ansible-playbook", "--version" ]

