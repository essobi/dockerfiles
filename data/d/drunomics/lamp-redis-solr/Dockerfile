FROM drunomics/lamp-redis:latest  
MAINTAINER drunomics GmbH <hello@drunomics.com>  
  
ADD requirements.yml /root/docker/lamp-redis-solr/  
ADD solr.yml /root/playbooks/  
  
RUN cd /root/docker/lamp-redis-solr && \  
ansible-galaxy install -r requirements.yml \--force && \  
  
# Fix issues with connecting to upstart, see  
# https://github.com/docker/docker/issues/1024  
dpkg-divert \--local \--rename \--add /sbin/initctl && ln -sf /bin/true
/sbin/initctl && \  
  
# Make sure apt sources are recent.  
apt-get update && \  
  
# Temporary fix for https://github.com/ansible/ansible/issues/5307,  
# remove once Ansible 1.9.0-2 is available.  
ln -s /etc/ansible/roles/drunomics.solr/files/1.6-solr-conf-4.x
/root/playbooks/1.6-solr-conf-4.x && \  
  
# Run the playbooks.  
cd /root/playbooks && \  
ansible-playbook solr.yml && \  
  
# Restore initctl.  
rm /sbin/initctl && cp /sbin/initctl.distrib /sbin/initctl && \  
  
# Clean tmp dirs.  
rm -rf /tmp/* /var/tmp/* && \  
  
# Save disk space by removing temporar solr files.  
rm -rf /root/solr-*  
  
VOLUME /var/data/solr

