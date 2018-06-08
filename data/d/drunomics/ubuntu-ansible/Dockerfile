FROM ubuntu-upstart:14.04  
MAINTAINER drunomics GmbH <hello@drunomics.com>  
  
# Install Ansible and Git.  
RUN apt-get update && \  
apt-get install python-support python-jinja2 python-yaml python-paramiko
python-httplib2 python-crypto sshpass software-properties-common -y && \  
add-apt-repository ppa:ansible/ansible-2.3 && apt-get update && \  
apt-get install ansible -y && \  
echo '[local]\nlocalhost ansible_connection=local\n' > /etc/ansible/hosts  
  
# Ensure security updates are installed.  
RUN unattended-upgrade -d  
  
RUN mkdir /root/.ssh && \  
ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts && \  
ssh-keyscan github.com >> /root/.ssh/known_hosts  

