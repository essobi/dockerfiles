FROM ubuntu:18.04  
LABEL maintainer="Jody Boucher"  
# Update packages data  
# Install base dependencies.  
# Add Ansible PPA  
# Install Ansible  
# Clean up  
RUN apt-get update && \  
apt-get install -y --no-install-recommends software-properties-common
python3-minimal systemd cron && \  
add-apt-repository -y ppa:ansible/ansible && \  
apt-get update && \  
apt-get install -y --no-install-recommends ansible && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/doc && \  
rm -rf /usr/share/man  
  
# Create Ansible inventory file with localhost  
RUN echo '[local]\nlocalhost ansible_connection=local\n' > /etc/ansible/hosts  

