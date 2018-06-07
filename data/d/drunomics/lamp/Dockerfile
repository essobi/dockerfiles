FROM drunomics/ubuntu-ansible  
MAINTAINER drunomics GmbH <hello@drunomics.com>  
  
# Install Ansible and Git.  
RUN apt-get update && \  
apt-get update && \  
apt-get install -y git  
  
RUN mkdir -p /root/.ssh && \  
ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts && \  
ssh-keyscan github.com >> /root/.ssh/known_hosts  
  
ADD requirements.yml /root/docker/lamp/  
ADD lamp.yml /root/playbooks/  
ADD vars/*.yml /etc/ansible/group_vars/all/  
  
RUN cd /root/docker/lamp && \  
ansible-galaxy install -r requirements.yml --force && \  
  
# Fix issues with connecting to upstart, see  
# https://github.com/docker/docker/issues/1024  
dpkg-divert --local --rename --add /sbin/initctl && ln -s /bin/true
/sbin/initctl && \  
  
# Run the playbooks  
cd /root/playbooks && \  
ansible-playbook lamp.yml && \  
  
# Restore initctl.  
rm /sbin/initctl && cp /sbin/initctl.distrib /sbin/initctl && \  
  
# Clean tmp dirs.  
rm -rf /tmp/* /var/tmp/* && \  
  
# Save disk space by removing inno db logfiles.  
rm -f /var/lib/mysql/ib_logfile*  
  
VOLUME /var/lib/mysql  

