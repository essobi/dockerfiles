FROM debian:jessie  
MAINTAINER Nathaniel Waisbrot <waisbrot@whoop.com>  
  
ENV ANSIBLE_VERSION 2.0.0.2  
ENV ANSIBLE_CONFIG /ansible.cfg  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends python python-pip python-crypto
openssh-client sshpass && \  
pip install ansible==${ANSIBLE_VERSION} boto ansible-lint python-dateutil
httplib2  
  
COPY ["ssh.py", "/usr/local/lib/python2.7/dist-
packages/ansible/plugins/connection/ssh.py"]  
  
ADD ansible.cfg run.sh /  
  
ENTRYPOINT ["/run.sh"]  

