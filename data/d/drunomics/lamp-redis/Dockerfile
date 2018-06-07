FROM drunomics/lamp:latest  
MAINTAINER drunomics GmbH <hello@drunomics.com>  
  
ADD requirements.yml /root/docker/lamp-redis/  
ADD redis.yml /root/playbooks/  
  
RUN cd /root/docker/lamp-redis && \  
ansible-galaxy install -r requirements.yml \--force && \  
  
# Fix issues with connecting to upstart, see  
# https://github.com/docker/docker/issues/1024  
dpkg-divert \--local \--rename \--add /sbin/initctl && ln -sf /bin/true
/sbin/initctl && \  
  
# Make sure apt sources are recent.  
apt-get update && \  
  
# Run the playbooks.  
cd /root/playbooks && \  
ansible-playbook redis.yml && \  
  
# Restore initctl.  
rm /sbin/initctl && cp /sbin/initctl.distrib /sbin/initctl && \  
  
# Clean tmp dirs.  
rm -rf /tmp/* /var/tmp/*  
  
VOLUME /var/lib/redis

