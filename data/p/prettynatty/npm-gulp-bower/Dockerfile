FROM ansible/ubuntu14.04-ansible:stable  
  
# Add playbooks to the Docker image  
ADD ansible /srv/ansible  
WORKDIR /srv/ansible  
  
# Install ansible requirements  
RUN ansible-galaxy install -r requirements.yml  
  
# Run Ansible to configure the Docker image  
RUN ansible-playbook site.yml -c local  
  
USER worker  

