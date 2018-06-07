# pull base image  
FROM alpine:3.6  
  
# Derived from https://github.com/William-Yeh/docker-ansible  
# Needed other versions of ansible, and saw no one has provided that.  
# Versions provided by pip are available. https://pypi.python.org/pypi/  
  
MAINTAINER Steve Louie <stephen.r.louie@gmail.com>  
  
  
RUN echo "===> Adding Python runtime..." && \  
apk --update add python py-pip openssl ca-certificates && \  
apk --update add \--virtual build-dependencies \  
python-dev libffi-dev openssl-dev build-base && \  
pip install --upgrade pip cffi && \  
\  
\  
echo "===> Installing Ansible..." && \  
pip install ansible==2.5.0b1 && \  
\  
\  
echo "===> Removing package list..." && \  
apk del build-dependencies && \  
rm -rf /var/cache/apk*  
  
  
# default command: display Ansible version  
CMD [ "ansible-playbook", "--version" ]  

